# Memento Pattern Practice

Memento is a behavioral design pattern that saves and restores an object's previous state without exposing its internal details.

Files:

- `behavioral/memento/example.py`: a form example that saves and restores username and email values
- `behavioral/memento/README.md`: short notes for this pattern

Example:

- `Memento`, `Originator`, and `Caretaker` are small interfaces for the pattern roles
- `FormOriginator` owns the form state and stores the current `username` and `email`
- `FormSnapshot` is the snapshot object that keeps a saved copy of the form fields
- `FormHistory` stores snapshots, shows history, and restores the most recent saved snapshot before removing it from history
- `FormOriginator.save()` creates a `FormSnapshot` for the current form values
- `FormOriginator.restore()` loads a previous `username` and `email` from a `Memento`
- the main block fills in the whole form, saves it, updates the whole form again, and then calls `undo()` twice to restore saved snapshots from newest to oldest

Advantages:

- keeps snapshot creation inside the object that owns the form state
- makes undo behavior simple for a small workflow
- separates state history management into `FormHistory`

Disadvantages:

- many snapshots can use extra memory if the form is saved too often
- Python cannot fully hide snapshot data the way some languages can
- adds extra classes for a very small form

When to use:

- when an object needs undo support for previous states
- when direct access to an object's data would hurt encapsulation
- when history management should be separate from the object being edited

Reference:

- https://refactoring.guru/design-patterns/memento
- https://refactoring.guru/design-patterns/memento/python/example
