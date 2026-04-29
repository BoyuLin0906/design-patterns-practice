# Visitor Pattern Practice

This folder shows a simple Visitor pattern example.

Visitor is a behavioral design pattern that lets you separate algorithms from the objects they work on. Each element accepts a visitor, and the visitor runs the right operation for that concrete element.

Files:

- `example.py`: three shapes that accept visitors for area, perimeter, and drawing
- `README.md`: short notes for this pattern

Example:

- `Circle`, `Rectangle`, and `Triangle` are the elements
- `accept` is the method that enables double dispatch
- `AreaVisitor`, `PerimeterVisitor`, and `DrawVisitor` are the visitors

Advantages:

- adds new operations without changing the shape classes
- keeps calculation and drawing logic outside the element classes
- works well when the same object structure needs multiple operations

Disadvantages:

- adding a new element type requires updating every visitor
- the pattern adds extra classes for simple cases

When to use:

- when you need multiple operations over a fixed set of object types
- when you want to keep auxiliary behavior out of the core classes
- when the same set of objects needs different kinds of processing

Reference:

- https://refactoring.guru/design-patterns/visitor
