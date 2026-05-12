from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class PersonContext:
    def __init__(self, name, country, age):
        self.name = name
        self.country = country
        self.age = age


class PersonExpression(ABC):
    @abstractmethod
    def interpret(self, context: PersonContext):
        raise NotImplementedError('Subclasses must implement interpret().')


# Terminal expression: checks one concrete country value.
class CountryIs(PersonExpression):
    def __init__(self, country):
        self.country = country

    def interpret(self, context: PersonContext):
        result = context.country == self.country
        print(f'CountryIs("{self.country}") -> {result}')
        return result


# Terminal expression: checks one minimum age rule.
class AgeAtLeast(PersonExpression):
    def __init__(self, minimum_age):
        self.minimum_age = minimum_age

    def interpret(self, context: PersonContext):
        result = context.age >= self.minimum_age
        print(f'AgeAtLeast({self.minimum_age}) -> {result}')
        return result


# Composite expression: combines two child expressions with AND.
class AndExpression(PersonExpression):
    def __init__(self, left: PersonExpression, right: PersonExpression):
        self.left: PersonExpression = left
        self.right: PersonExpression = right

    def interpret(self, context: PersonContext):
        left_result = self.left.interpret(context)
        right_result = self.right.interpret(context)
        result = left_result and right_result
        print(f'AndExpression -> {result}')
        return result


class PersonRuleChecker:
    def __init__(self, rule: PersonExpression):
        self.rule: PersonExpression = rule

    def matches(self, context: PersonContext):
        return self.rule.interpret(context)


def show_result(title, checker: PersonRuleChecker, person: PersonContext):
    print_section(title)
    result = checker.matches(person)
    print(f'name={person.name} | country={person.country} | age={person.age}')
    print(f'matches rule: {result}')


if __name__ == '__main__':
    is_from_taiwan = CountryIs('TW')
    is_adult = AgeAtLeast(18)
    taiwan_adult_rule = AndExpression(is_from_taiwan, is_adult)
    checker = PersonRuleChecker(taiwan_adult_rule)

    amy = PersonContext(name='Amy', country='TW', age=20)
    ben = PersonContext(name='Ben', country='TW', age=16)
    chris = PersonContext(name='Chris', country='JP', age=22)

    print_section('Rule')
    print('country is TW AND age is at least 18')

    show_result('Adult In Taiwan', checker, amy)
    show_result('Too Young In Taiwan', checker, ben)
    show_result('Adult In Another Country', checker, chris)
