# Object Pool Pattern Practice

Object Pool is a creational design pattern that reuses a small set of expensive objects instead of creating a new one every time.

Files:

- `creational/object_pool/example.py`: a database connection pool with explicit checkout and return
- `creational/object_pool/README.md`: short notes for this pattern

Example:

- `DatabaseConnection` is the reusable object
- `DatabaseConnectionPool` creates connections only when needed and keeps returned ones in an internal list
- `acquire_connection()` gives a connection to the client, and `release_connection()` puts it back into the pool
- the main block shows one connection being borrowed, returned, and borrowed again before the pool limit is reached

Advantages:

- avoids repeatedly creating expensive objects such as database connections
- centralizes reuse rules in one place
- makes a fixed pool size easy to enforce

Disadvantages:

- adds lifecycle management that simple code may not need
- can leak resources if clients forget to return objects
- can become more complex when waiting, timeouts, or thread safety are required

When to use:

- when object creation is relatively expensive
- when only a small number of reusable resources should exist at once
- when clients repeatedly borrow and return the same kind of object

Context manager note:

- a context manager can be a good Python wrapper for automatic release, especially for database connections
- this example keeps acquire and release explicit so the pattern itself stays easy to see

Reference:

- https://sourcemaking.com/design_patterns/object_pool
