from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        raise NotImplementedError('Subclasses must implement log().')


class ConsoleLogger(Logger):
    def log(self, message):
        print(f'[LOG] {message}')


class NullLogger(Logger):
    def log(self, message):
        pass


class UserImporter:
    def __init__(self, logger: Logger):
        self.logger: Logger = logger

    def import_user(self, name, email):
        self.logger.log(f'Start import for {name}.')
        print(f'Importing user: {name} <{email}>')
        self.logger.log(f'Finished import for {name}.')


if __name__ == '__main__':
    print_section('With Real Logger')
    importer_with_logs = UserImporter(logger=ConsoleLogger())
    importer_with_logs.import_user('Alice', 'alice@example.com')

    print_section('With Null Logger')
    importer_without_logs = UserImporter(logger=NullLogger())
    importer_without_logs.import_user('Bob', 'bob@example.com')

