from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class ValidationHandler(ABC):
    def __init__(self):
        self._next_handler: ValidationHandler | None = None

    def set_next(self, handler: ValidationHandler) -> ValidationHandler:
        self._next_handler = handler
        return handler

    def handle(self, value):
        if not self.check(value):
            print('*** STOP ***')
            return False

        if self._next_handler is None:
            print('*** DONE ***')
            return True

        return self._next_handler.handle(value)

    @abstractmethod
    def check(self, value):
        raise NotImplementedError('Subclasses must implement check().')


class CheckIntHandler(ValidationHandler):
    def check(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            print('check int: fail')
            return False

        print('check int: ok')
        return True


class CheckPositiveHandler(ValidationHandler):
    def check(self, value):
        if value <= 0:
            print('check positive: fail')
            return False

        print('check positive: ok')
        return True


class CheckEvenNumberHandler(ValidationHandler):
    def check(self, value):
        if value % 2 != 0:
            print('check even number: fail')
            return False

        print('check even number: ok')
        return True


def run_validation(title, validator, value):
    print(f'{title} (value: {value!r})')

    is_valid = validator.handle(value)
    print(f'result: {"valid" if is_valid else "invalid"}')
    print()


def build_full_validation_chain():
    check_int = CheckIntHandler()
    check_positive = CheckPositiveHandler()
    check_even_number = CheckEvenNumberHandler()

    check_int.set_next(check_positive).set_next(check_even_number)
    return check_int


def build_even_only_chain():
    check_int = CheckIntHandler()
    check_even_number = CheckEvenNumberHandler()

    check_int.set_next(check_even_number)
    return check_int


if __name__ == '__main__':
    full_chain = build_full_validation_chain()
    even_only_chain = build_even_only_chain()

    print_section('Full Chain With Valid Number')
    run_validation(
        'Chain 1: check_int -> check_positive -> check_even_number',
        full_chain,
        8,
    )
    print_section('Full Chain With Negative Number')
    run_validation(
        'Chain 1: check_int -> check_positive -> check_even_number',
        full_chain,
        -4,
    )
    print_section('Even Only Chain With Negative Number')
    run_validation(
        'Chain 2: check_int -> check_even_number',
        even_only_chain,
        -4,
    )
    print_section('Even Only Chain With String Value')
    run_validation(
        'Chain 2: check_int -> check_even_number',
        even_only_chain,
        '12',
    )
