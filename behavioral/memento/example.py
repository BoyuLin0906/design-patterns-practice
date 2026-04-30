from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class Memento(ABC):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError('Subclasses must implement get_name().')


class FormSnapshot(Memento):
    def __init__(self, label, username, email):
        self._label = label
        self._username = username
        self._email = email

    def get_name(self):
        return self._label


class Originator(ABC):
    @abstractmethod
    def save(self, label):
        raise NotImplementedError('Subclasses must implement save().')

    @abstractmethod
    def restore(self, memento: Memento):
        raise NotImplementedError('Subclasses must implement restore().')


class FormOriginator(Originator):
    def __init__(self):
        self.username = ''
        self.email = ''

    def set_username(self, username):
        self.username = username
        print(f'Username field updated to: {self.username}')

    def set_email(self, email):
        self.email = email
        print(f'Email field updated to: {self.email}')

    def save(self, label):
        return FormSnapshot(label, self.username, self.email)

    def restore(self, memento: Memento):
        self.username = memento._username
        self.email = memento._email
        print(f'Form restored to snapshot: {memento.get_name()}')

    def show_form(self):
        print(f'username={self.username or "(empty)"} | email={self.email or "(empty)"}')


class Caretaker(ABC):
    @abstractmethod
    def backup(self, label):
        raise NotImplementedError('Subclasses must implement backup().')

    @abstractmethod
    def undo(self):
        raise NotImplementedError('Subclasses must implement undo().')


class FormHistory(Caretaker):
    def __init__(self, originator: Originator):
        self.originator: Originator = originator
        self._history: list[Memento] = []

    def backup(self, label):
        snapshot = self.originator.save(label)
        self._history.append(snapshot)
        print(f'FormHistory: saved snapshot "{snapshot.get_name()}".')

    def undo(self):
        if len(self._history) < 1:
            print('FormHistory: no snapshot to restore.')
            return

        latest_snapshot = self._history.pop()
        print(f'FormHistory: restoring snapshot "{latest_snapshot.get_name()}".')
        self.originator.restore(latest_snapshot)

    def show_history(self):
        print('Saved snapshots:')
        for snapshot in self._history:
            print(f'- {snapshot.get_name()}')


if __name__ == '__main__':
    form = FormOriginator()
    history = FormHistory(form)

    print_section('Save First Version')
    form.set_username('andylin')
    form.set_email('andy@example.com')
    form.show_form()
    history.backup('First saved form')

    print_section('Save Updated Version')
    form.set_username('andy.lin')
    form.set_email('andy.lin@example.com')
    form.show_form()
    history.backup('Updated saved form')

    print_section('History')
    history.show_history()

    print_section('Undo Last Change')
    history.undo()
    form.show_form()

    print_section('Undo Again')
    history.undo()
    form.show_form()
