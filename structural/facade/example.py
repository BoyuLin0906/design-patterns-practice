from __future__ import annotations

import csv
import json
import tempfile
from abc import ABC, abstractmethod
from pathlib import Path


def print_section(title):
    print(f'\n=== {title} ===')


class RecordReader(ABC):
    @abstractmethod
    def read_records(self, file_path):
        raise NotImplementedError('Subclasses must implement read_records().')


class CsvFileReader(RecordReader):
    def read_records(self, file_path):
        print(f'CsvFileReader: reading {file_path.name}')
        with file_path.open(newline='', encoding='utf-8') as csv_file:
            return list(csv.DictReader(csv_file))


class JsonFileReader(RecordReader):
    def read_records(self, file_path):
        print(f'JsonFileReader: reading {file_path.name}')
        with file_path.open(encoding='utf-8') as json_file:
            return json.load(json_file)


class RecordValidator:
    required_fields = ['customer_id', 'name', 'email', 'status']

    def validate(self, raw_records):
        print('RecordValidator: validating records')

        valid_records = []
        for index, record in enumerate(raw_records, start=1):
            missing_fields = [
                field for field in self.required_fields if not record.get(field)
            ]

            if missing_fields:
                print(
                    f'Skipping record {index}: missing {", ".join(missing_fields)}'
                )
                continue

            valid_records.append(record)

        return valid_records


class RecordTransformer:
    def transform(self, valid_records):
        print('RecordTransformer: transforming records')

        transformed_records = []
        for record in valid_records:
            transformed_records.append(
                {
                    'customer_id': record['customer_id'].strip(),
                    'display_name': record['name'].strip().title(),
                    'email': record['email'].strip().lower(),
                    'status': record['status'].strip().upper(),
                }
            )

        return transformed_records


class CustomerDatabase:
    def __init__(self):
        self.saved_records = []

    def save_many(self, records):
        print(f'CustomerDatabase: saving {len(records)} record(s)')
        self.saved_records.extend(records)

    def show_all(self):
        for record in self.saved_records:
            print(record)


class DataImportFacade:
    def __init__(
        self,
        reader: RecordReader,
        validator: RecordValidator,
        transformer: RecordTransformer,
        database: CustomerDatabase,
    ):
        self.reader: RecordReader = reader
        self.validator: RecordValidator = validator
        self.transformer: RecordTransformer = transformer
        self.database: CustomerDatabase = database

    def import_file(self, file_path):
        path = Path(file_path)
        raw_records = self.reader.read_records(path)
        valid_records = self.validator.validate(raw_records)
        transformed_records = self.transformer.transform(valid_records)
        self.database.save_many(transformed_records)

        print(
            f'DataImportFacade: imported {len(transformed_records)} record(s) '
            f'from {path.name}'
        )


def write_csv_sample(file_path):
    rows = [
        {
            'customer_id': 'c-101',
            'name': 'alice chen',
            'email': 'ALICE@EXAMPLE.COM',
            'status': 'active',
        },
        {
            'customer_id': 'c-102',
            'name': '',
            'email': 'missing-name@example.com',
            'status': 'inactive',
        },
    ]

    with file_path.open('w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def write_json_sample(file_path):
    rows = [
        {
            'customer_id': 'c-201',
            'name': 'bob lin',
            'email': 'bob@example.com',
            'status': 'pending',
        },
        {
            'customer_id': 'c-202',
            'name': 'carol wu',
            'email': '',
            'status': 'active',
        },
    ]

    with file_path.open('w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=2)


if __name__ == '__main__':
    database = CustomerDatabase()
    validator = RecordValidator()
    transformer = RecordTransformer()

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        csv_file = temp_path / 'customers.csv'
        json_file = temp_path / 'customers.json'

        write_csv_sample(csv_file)
        write_json_sample(json_file)

        print_section('Import CSV File')
        csv_import_facade = DataImportFacade(
            CsvFileReader(),
            validator,
            transformer,
            database,
        )
        csv_import_facade.import_file(csv_file)

        print_section('Import JSON File')
        json_import_facade = DataImportFacade(
            JsonFileReader(),
            validator,
            transformer,
            database,
        )
        json_import_facade.import_file(json_file)

        print_section('Saved Records In Database')
        database.show_all()
