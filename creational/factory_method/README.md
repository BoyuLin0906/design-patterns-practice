# Factory Method Pattern Practice

Factory Method is a creational design pattern that defines a method for creating an object in a base class while letting subclasses decide which concrete object to return.

Files:

- `creational/factory_method/example.py`: a database connection example with MySQL and PostgreSQL creators
- `creational/factory_method/README.md`: short notes for this pattern

Example:

- `DatabaseConnection` is the shared product interface for all database connections
- `MySQLConnection` and `PostgreSQLConnection` are the concrete products
- `DatabaseFactory` is the creator that declares `create_connection()`
- `MySQLFactory` and `PostgreSQLFactory` are the concrete creators that return different connection objects
- `show_preview()` receives a `DatabaseConnection` object directly, so the created product is injected into the client code before use

Advantages:

- separates database connection creation from the code that uses the connection
- makes it easy to add another database by creating one product and one factory subclass
- keeps client code dependent on shared abstractions instead of concrete database classes

Disadvantages:

- adds extra classes for a small example
- uses inheritance, which can feel heavier than direct construction
- may be unnecessary when object creation never varies

When to use:

- when the code should work with a product interface, but you do not know all concrete product types in advance
- when you want subclasses or framework users to extend which concrete product gets created
- when object creation should be centralized so expensive resources, such as database connections, can be created or reused in one place

Reference:

- https://refactoring.guru/design-patterns/factory-method
