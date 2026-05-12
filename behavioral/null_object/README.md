# Null Object Pattern Practice

This folder shows a simple Null Object pattern example.

Null Object is a behavioral design pattern that replaces a missing collaborator with a special object that has the same interface but safely does nothing.

Files:

- `behavioral/null_object/example.py`: a user importer that can work with a real logger or a do-nothing logger
- `behavioral/null_object/README.md`: short notes for this pattern

Example:

- `Logger` is the shared interface for logging
- `ConsoleLogger` is the real object that prints log messages
- `NullLogger` is the null object that accepts log calls and does nothing
- `UserImporter` is the client that always talks to a `Logger` and never checks for `None`
- the example runs the importer once with `ConsoleLogger` and once with `NullLogger`

Advantages:

- removes repeated `None` checks from client code
- keeps optional behavior behind the same interface
- makes client code simpler to read

Disadvantages:

- adds an extra class for do-nothing behavior
- can hide mistakes if silence is not the right default
- may be unnecessary for very small code paths

When to use:

- when a client expects a collaborator but some cases should do nothing
- when you want to avoid repeated null checks
- when a safe default behavior is clearer than branching logic

Reference:

- https://sourcemaking.com/design_patterns/null_object
