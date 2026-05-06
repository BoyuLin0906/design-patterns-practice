from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError('Subclasses must implement connect().')

    @abstractmethod
    def run_query(self, query):
        raise NotImplementedError('Subclasses must implement run_query().')


class MySQLConnection(DatabaseConnection):
    def connect(self):
        print('Connect to MySQL on port 3306')

    def run_query(self, query):
        print(f'MySQL executes: {query}')


class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print('Connect to PostgreSQL on port 5432')

    def run_query(self, query):
        print(f'PostgreSQL executes: {query}')


class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self):
        raise NotImplementedError('Subclasses must implement create_connection().')


class MySQLFactory(DatabaseFactory):
    def create_connection(self):
        return MySQLConnection()


class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self):
        return PostgreSQLConnection()


def show_preview(connection: DatabaseConnection):
    connection.connect()
    connection.run_query('SELECT id, name FROM users LIMIT 3')


if __name__ == '__main__':
    mysql_factory = MySQLFactory()
    postgresql_factory = PostgreSQLFactory()
    mysql_connection = mysql_factory.create_connection()
    postgresql_connection = postgresql_factory.create_connection()

    print_section('MySQL Preview')
    show_preview(mysql_connection)

    print_section('PostgreSQL Preview')
    show_preview(postgresql_connection)
