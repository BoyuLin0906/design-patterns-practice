from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class UserService(ABC):
    @abstractmethod
    def get_user(self, user_id):
        raise NotImplementedError('Subclasses must implement get_user().')


class DatabaseUserService(UserService):
    def __init__(self):
        self.users = {
            1: {'id': 1, 'name': 'Alice', 'role': 'admin'},
            2: {'id': 2, 'name': 'Bob', 'role': 'member'},
        }

    def get_user(self, user_id):
        print(f'DatabaseUserService: loading user {user_id} from database')
        return self.users.get(user_id)


class UserServiceDecorator(UserService):
    def __init__(self, service: UserService):
        self.service: UserService = service

    def get_user(self, user_id):
        return self.service.get_user(user_id)


class CacheUserService(UserServiceDecorator):
    def __init__(self, service: UserService):
        super().__init__(service)
        self.cache = {}

    def get_user(self, user_id):
        if user_id in self.cache:
            print(f'CacheUserService: returning cached user {user_id}')
            return self.cache[user_id]

        user = super().get_user(user_id)
        if user is not None:
            print(f'CacheUserService: saving user {user_id} in cache')
            self.cache[user_id] = user

        return user


class LogUserService(UserServiceDecorator):
    def get_user(self, user_id):
        print(f'LogUserService: get_user({user_id}) called')
        user = super().get_user(user_id)

        if user is None:
            print(f'LogUserService: user {user_id} was not found')
        else:
            print(f'LogUserService: returning user {user["name"]}')

        return user


if __name__ == '__main__':
    user_service = LogUserService(CacheUserService(DatabaseUserService()))

    print_section('First Request')
    print(user_service.get_user(1))

    print_section('Second Request Uses Cache')
    print(user_service.get_user(1))

    print_section('Missing User')
    print(user_service.get_user(99))
