from abc import ABC, abstractmethod
from dataclasses import dataclass


def print_section(title):
    print(f'\n=== {title} ===')


@dataclass
class UserData:
    user_id: int
    name: str
    email: str

    def show(self):
        print(f'User #{self.user_id}: {self.name} <{self.email}>')


class UserReader(ABC):
    @abstractmethod
    def get_user(self, user_id):
        raise NotImplementedError('Subclasses must implement get_user().')


class DatabaseUserService(UserReader):
    def __init__(self, users: dict[int, UserData]):
        self._connected = False
        self._users = users

    def _connect(self):
        if not self._connected:
            print('Open database connection')
            self._connected = True

    def get_user(self, user_id):
        self._connect()
        print(f'Database query for user #{user_id}')
        return self._users.get(user_id)


class AuthorizedUserProxy(UserReader):
    def __init__(self, service: UserReader, current_role):
        self.service = service
        self.current_role = current_role

    def get_user(self, user_id):
        if self.current_role != 'admin':
            print(f'Access denied for role: {self.current_role}')
            return None

        print(f'Access granted for role: {self.current_role}')
        return self.service.get_user(user_id)


class CachedUserProxy(UserReader):
    def __init__(self, service: UserReader):
        self.service = service
        self.cache = {}

    def get_user(self, user_id):
        if user_id in self.cache:
            print(f'Cache hit for user #{user_id}')
            return self.cache[user_id]

        print(f'Cache miss for user #{user_id}')
        user = self.service.get_user(user_id)

        if user is not None:
            self.cache[user_id] = user

        return user


def show_user(user_reader: UserReader, user_id):
    user = user_reader.get_user(user_id)

    if user is None:
        print(f'Could not load user #{user_id}')
        return

    user.show()


if __name__ == '__main__':
    fake_users = {
        1: UserData(1, 'Ava Chen', 'ava@example.com'),
        2: UserData(2, 'Noah Kim', 'noah@example.com'),
        3: UserData(3, 'Mia Lopez', 'mia@example.com'),
    }
    database_service = DatabaseUserService(fake_users)
    cached_database = CachedUserProxy(database_service)

    print_section('Unauthorized Request')
    guest_reader = AuthorizedUserProxy(
        cached_database, 'guest'
    )
    show_user(guest_reader, 1)

    print_section('First Authorized Request')
    admin_reader = AuthorizedUserProxy(
        cached_database, 'admin'
    )
    show_user(admin_reader, 2)

    print_section('Repeat Authorized Request')
    show_user(admin_reader, 2)

    print_section('Missing User')
    show_user(admin_reader, 99)
