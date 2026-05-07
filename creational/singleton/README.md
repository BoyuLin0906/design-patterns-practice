# Singleton Pattern Practice

Singleton is a creational design pattern that ensures a class has only one instance and provides a global access point to it.

Files:

- `creational/singleton/example.py`: a logger example with one shared logger instance
- `creational/singleton/README.md`: short notes for this pattern

Example:

- `Logger` is the singleton class that stores log entries and logger state
- `Logger.get_instance()` is the single access point that creates the logger once and returns the same object later
- `configure()` sets the logger level and format once during startup
- `log()` shows that different parts of the program reuse the same configured logger
- `show_history()` prints the stored log entries so the shared instance is easy to verify

Advantages:

- guarantees that only one logger object is created
- gives different parts of the program one shared access point to logging
- delays creation until the logger is first needed
- matches the common startup pattern where logging is configured once for the whole process

Disadvantages:

- introduces global shared state, which can make testing harder
- can hide design problems if too many parts of the program depend on the singleton
- needs extra care in multithreaded code
- is too rigid when different parts of the system need different logger settings

When to use:

- when the program should share one object, such as a logger, config loader, or cache
- when you want one place to control access to a shared resource
- when creating multiple copies of the same service would be wasteful or confusing
- when process-wide settings should be configured once and then reused everywhere

Reference:

- https://refactoring.guru/design-patterns/singleton
