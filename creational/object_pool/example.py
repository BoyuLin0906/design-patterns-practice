def print_section(title):
    print(f'\n=== {title} ===')


class DatabaseConnection:
    def __init__(self, connection_id):
        self.connection_id = connection_id

    def run_query(self, query):
        print(f'Connection #{self.connection_id} executes: {query}')

    def reset(self):
        print(f'Connection #{self.connection_id} returned to the pool')


class DatabaseConnectionPool:
    def __init__(self, max_size):
        self.max_size = max_size
        self._available = []
        self._in_use = set()
        self._next_connection_id = 1

    def acquire_connection(self):
        if self._available:
            connection = self._available.pop()
            print(f'Reuse connection #{connection.connection_id} from the pool')
        elif self.total_connections() < self.max_size:
            connection = DatabaseConnection(self._next_connection_id)
            self._next_connection_id += 1
            print(f'Create new connection #{connection.connection_id}')
        else:
            raise RuntimeError('No connection available in the pool right now.')

        self._in_use.add(connection)
        return connection

    def release_connection(self, connection: DatabaseConnection):
        if connection not in self._in_use:
            raise RuntimeError('This connection does not belong to the active pool.')

        self._in_use.remove(connection)
        connection.reset()
        self._available.append(connection)

    def total_connections(self):
        return len(self._available) + len(self._in_use)

    def show_status(self):
        available_ids = [connection.connection_id for connection in self._available]
        in_use_ids = [connection.connection_id for connection in self._in_use]
        print(f'max_size={self.max_size}')
        print(f'available={available_ids}')
        print(f'in_use={sorted(in_use_ids)}')


if __name__ == '__main__':
    pool = DatabaseConnectionPool(max_size=2)

    print_section('Initial Pool')
    pool.show_status()

    print_section('Take A Connection')
    first_connection = pool.acquire_connection()
    first_connection.run_query('SELECT * FROM users')
    pool.show_status()

    print_section('Return It')
    pool.release_connection(first_connection)
    pool.show_status()

    print_section('Take It Again')
    reused_connection = pool.acquire_connection()
    reused_connection.run_query('SELECT * FROM orders')
    print(
        'Reused the same object:',
        reused_connection is first_connection,
    )
    pool.show_status()

    print_section('Pool Limit')
    second_connection = pool.acquire_connection()

    try:
        pool.acquire_connection()
    except RuntimeError as error:
        print(error)

    print_section('Return Connections')
    pool.release_connection(reused_connection)
    pool.release_connection(second_connection)
    pool.show_status()
