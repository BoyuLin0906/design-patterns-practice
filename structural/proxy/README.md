# Proxy Pattern Practice

Proxy is a structural design pattern that provides a stand-in object which controls access to a real subject.

Files:

- `structural/proxy/example.py`: a user lookup example with a database service wrapped by auth and cache proxies
- `structural/proxy/README.md`: short notes for this pattern

Example:

- `UserReader` is the shared interface used by both the real service and the proxies
- `DatabaseUserService` is the real subject, receives the fake database from outside, and performs the user lookup
- `AuthorizedUserProxy` is a protection proxy that blocks access unless the role is `admin`
- `CachedUserProxy` is a caching proxy that stores previously loaded users by `user_id`
- `show_user()` is a small helper that keeps the main block readable while calling the shared `UserReader` interface
- the main block shows a denied request, a database-backed request, a cached repeat request, and a missing user lookup

Advantages:

- controls access to the database without changing `DatabaseUserService`
- adds caching without changing the client code
- keeps the client dependent on one shared interface

Disadvantages:

- adds more classes and another layer of delegation
- can make the request flow less direct to trace
- stacked proxies can add extra runtime steps

When to use:

- when you need access control around a service object
- when expensive requests should be cached behind the same interface
- when clients should not know whether they talk to a real service or a stand-in object

Reference:

- https://refactoring.guru/design-patterns/proxy
