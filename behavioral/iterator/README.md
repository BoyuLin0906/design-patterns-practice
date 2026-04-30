# Iterator Pattern Practice

Iterator is a behavioral design pattern that lets you traverse a collection without exposing its internal structure.

Files:

- `behavioral/iterator/example.py`: a page collection with explicit forward and reverse iterators
- `behavioral/iterator/README.md`: short notes for this pattern

Example:

- `DataIterator` is the iterator abstraction with explicit methods like `has_next()`, `next_items()`, and `reset()`
- `DataCollection` is the collection abstraction that exposes stored items and creates iterators
- `PageDataCollection` is the concrete collection that receives page data from outside
- `ForwardIterator` reads items from the beginning in groups
- `ReverseIterator` reads items from the end in groups
- the main block creates the collection, asks it for two iterators, and shows that `reset()` lets an iterator start over
- `example.py` avoids magic methods like `__iter__()` and `__next__()` so each traversal step stays explicit for practice

Note:

- in real projects, iterator behavior is often implemented with language-specific magic methods
- this practice example uses explicit methods instead, so the pattern structure is easier to see

Advantages:

- separates traversal logic from collection storage
- allows different traversal strategies for the same collection
- makes batch size a clear iterator-level concern

Disadvantages:

- adds more classes than a direct loop
- simple collections may not need separate iterators
- many traversal variations can increase the number of classes

When to use:

- when a collection has an internal structure you want to hide from client code
- when traversal logic would otherwise be duplicated across different parts of the application
- when client code should work with different collections or traversal styles through the same interfaces

Reference:

- https://refactoring.guru/design-patterns/iterator
