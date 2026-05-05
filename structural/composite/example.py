from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class FileSystemNode(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_size(self):
        raise NotImplementedError('Subclasses must implement get_size().')

    def show(self, indent=0):
        raise NotImplementedError('Subclasses must implement show().')


class FileItem(FileSystemNode):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_size(self):
        return self.size

    def show(self, indent=0):
        print(f'{" " * indent}- file: {self.name} ({self.get_size()} KB)')


class Folder(FileSystemNode):
    def __init__(self, name):
        super().__init__(name)
        self.children: list[FileSystemNode] = []

    def add(self, child: FileSystemNode):
        self.children.append(child)

    def remove(self, child: FileSystemNode):
        self.children.remove(child)

    def get_size(self):
        return sum(child.get_size() for child in self.children)

    def show(self, indent=0):
        print(f'{" " * indent}+ folder: {self.name} ({self.get_size()} KB)')
        for child in self.children:
            child.show(indent + 2)


if __name__ == '__main__':
    resume = FileItem('resume.pdf', 120)
    photo = FileItem('photo.jpg', 850)
    budget = FileItem('budget.xlsx', 300)
    invoice = FileItem('invoice.pdf', 180)

    documents = Folder('documents')
    pictures = Folder('pictures')
    work = Folder('work')
    home = Folder('home')

    documents.add(resume)
    pictures.add(photo)
    work.add(budget)
    work.add(invoice)

    documents.add(work)

    home.add(documents)
    home.add(pictures)

    print_section('Initial File Tree')
    home.show()

    print_section('Initial Total Size')
    print(f'Home folder total size: {home.get_size()} KB')

    print_section('Remove A File')
    work.remove(invoice)
    home.show()
    print(f'Home folder total size after removal: {home.get_size()} KB')

    print_section('Add A New Folder')
    archive = Folder('archive')
    archive.add(FileItem('tax_2024.pdf', 640))
    archive.add(FileItem('notes.txt', 20))
    documents.add(archive)
    home.show()
    print(f'Home folder total size after adding archive: {home.get_size()} KB')
