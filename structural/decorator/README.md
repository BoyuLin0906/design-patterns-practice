# Decorator Pattern Practice

Decorator is a structural design pattern that adds behavior to an object by wrapping it with other objects that follow the same interface.

Files:

- `structural/decorator/example.py`: a user service example with logging and caching decorators around one `get_user()` operation
- `structural/decorator/README.md`: short notes for this pattern

Example:

- `UserService` is the shared interface used by both the core service and all decorators
- `DatabaseUserService` is the concrete component and simulates loading users from a database
- `UserServiceDecorator` is the base decorator that stores the wrapped service and delegates `get_user()`
- `CacheUserService` returns a saved user when it is already in cache and only calls the wrapped service on a cache miss
- `LogUserService` adds log messages before and after each `get_user()` call without changing the interface

Advantages:

- lets you add caching or logging without changing the core user service
- keeps each extra behavior focused in its own class
- makes it easy to combine wrappers in different orders

Disadvantages:

- adds more small classes for a simple flow
- behavior can change depending on the order of decorators

When to use:

- when you want to add optional behaviors around an existing object
- when inheritance would create too many special-case subclasses
- when clients should keep using the same interface after extra behavior is added

Reference:

- https://refactoring.guru/design-patterns/decorator
