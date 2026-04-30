from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class DataIterator(ABC):
    @abstractmethod
    def has_next(self):
        raise NotImplementedError('Subclasses must implement has_next().')

    @abstractmethod
    def next_items(self):
        raise NotImplementedError('Subclasses must implement next_items().')

    @abstractmethod
    def reset(self):
        raise NotImplementedError('Subclasses must implement reset().')


class DataCollection(ABC):
    @abstractmethod
    def get_items(self):
        raise NotImplementedError('Subclasses must implement get_items().')

    @abstractmethod
    def create_forward_iterator(self, size):
        raise NotImplementedError(
            'Subclasses must implement create_forward_iterator().'
        )

    @abstractmethod
    def create_reverse_iterator(self, size):
        raise NotImplementedError(
            'Subclasses must implement create_reverse_iterator().'
        )


class PageDataCollection(DataCollection):
    def __init__(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def create_forward_iterator(self, size):
        return ForwardIterator(self, size)

    def create_reverse_iterator(self, size):
        return ReverseIterator(self, size)


class ForwardIterator(DataIterator):
    def __init__(self, collection: DataCollection, size):
        self.collection: DataCollection = collection
        self.size = max(1, size)
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection.get_items())

    def next_items(self):
        if not self.has_next():
            return []

        end_index = self.index + self.size
        batch = self.collection.get_items()[self.index:end_index]
        self.index += len(batch)
        return batch

    def reset(self):
        self.index = 0


class ReverseIterator(DataIterator):
    def __init__(self, collection: DataCollection, size):
        self.collection: DataCollection = collection
        self.size = max(1, size)
        self.index = len(self.collection.get_items())

    def has_next(self):
        return self.index > 0

    def next_items(self):
        if not self.has_next():
            return []

        start_index = max(self.index - self.size, 0)
        batch = self.collection.get_items()[start_index:self.index]
        batch.reverse()
        self.index -= len(batch)
        return batch

    def reset(self):
        self.index = len(self.collection.get_items())
if __name__ == '__main__':
    items = [
        'page 1',
        'page 2',
        'page 3',
        'page 4',
        'page 5',
        'page 6',
    ]
    page_data = PageDataCollection(items)

    forward_iterator = page_data.create_forward_iterator(size=2)
    reverse_iterator = page_data.create_reverse_iterator(size=3)

    print_section('Forward Iterator')
    while forward_iterator.has_next():
        print(forward_iterator.next_items())

    print_section('Reverse Iterator')
    while reverse_iterator.has_next():
        print(reverse_iterator.next_items())

    print_section('Reset Forward Iterator')
    forward_iterator.reset()
    print(forward_iterator.next_items())
