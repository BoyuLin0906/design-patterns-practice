from abc import ABC, abstractmethod
import json


def print_section(title):
    print(f'\n=== {title} ===')


TXT_SOURCE = 'Quarterly revenue increased by 15 percent after the product launch.'

CSV_SOURCE = [
    ['region', 'sales', 'profit'],
    ['North', '1200', '210'],
    ['South', '980', '180'],
    ['West', '1430', '260'],
]

PDF_SOURCE = {
    'title': 'Incident Report',
    'pages': [
        'Page 1: Server outage started at 09:10.',
        'Page 2: Recovery completed at 09:42.',
    ],
}


class DocumentETL(ABC):
    def run(self, source_name, source_data):
        print(f'Process: {source_name}')
        raw_data = self.extract(source_data)
        transformed_data = self.transform(raw_data, source_name)
        json_output = self.load(transformed_data)
        self.print_result(json_output)

    @abstractmethod
    def extract(self, source_data):
        raise NotImplementedError('Subclasses must implement extract().')

    @abstractmethod
    def transform(self, raw_data, source_name):
        raise NotImplementedError('Subclasses must implement transform().')

    def load(self, transformed_data):
        return json.dumps(transformed_data, indent=2)

    def print_result(self, json_output):
        print('JSON output:')
        print(json_output)
        print()


class TxtDocumentETL(DocumentETL):
    def extract(self, source_data):
        return source_data

    def transform(self, raw_data, source_name):
        words = raw_data.replace('.', '').split()
        return {
            'source_name': source_name,
            'document_type': 'txt',
            'summary': raw_data,
            'metadata': {
                'record_count': 1,
                'word_count': len(words),
                'keywords': words[:5],
            },
            'records': [
                {
                    'section': 'body',
                    'text': raw_data,
                }
            ],
        }


class CsvDocumentETL(DocumentETL):
    def extract(self, source_data):
        return source_data

    def transform(self, raw_data, source_name):
        headers = raw_data[0]
        rows = [dict(zip(headers, row)) for row in raw_data[1:]]
        total_sales = sum(int(row['sales']) for row in rows)

        return {
            'source_name': source_name,
            'document_type': 'csv',
            'summary': f'{len(rows)} sales records loaded.',
            'metadata': {
                'record_count': len(rows),
                'total_sales': total_sales,
                'columns': headers,
            },
            'records': rows,
        }


class PdfDocumentETL(DocumentETL):
    def extract(self, source_data):
        return source_data

    def transform(self, raw_data, source_name):
        page_summaries = [page.split(': ', 1)[1] for page in raw_data['pages']]

        return {
            'source_name': source_name,
            'document_type': 'pdf',
            'summary': ' '.join(page_summaries),
            'metadata': {
                'record_count': len(page_summaries),
                'title': raw_data['title'],
                'page_count': len(raw_data['pages']),
            },
            'records': [
                {
                    'page': index,
                    'text': page_summary,
                }
                for index, page_summary in enumerate(page_summaries, start=1)
            ],
        }


if __name__ == '__main__':
    txt_pipeline = TxtDocumentETL()
    csv_pipeline = CsvDocumentETL()
    pdf_pipeline = PdfDocumentETL()

    print_section('Process TXT Document')
    txt_pipeline.run('summary.txt', TXT_SOURCE)
    print_section('Process CSV Document')
    csv_pipeline.run('sales.csv', CSV_SOURCE)
    print_section('Process PDF Document')
    pdf_pipeline.run('incident_report.pdf', PDF_SOURCE)
