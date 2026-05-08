# Builder Pattern Practice

Builder is a creational design pattern that constructs a complex object step by step so the creation logic stays separate from the final object.

Files:

- `creational/builder/example.py`: an app configuration example with local and production build flows
- `creational/builder/README.md`: short notes for this pattern

Example:

- `AppConfig` is the product that stores many app settings such as `host`, `port`, `debug_mode`, and `database_url`, with boolean flags defaulting to `False`
- `AppConfigBuilder` is the builder interface that defines the configuration steps
- `EnvironmentConfigBuilder` is the concrete builder that fills an `AppConfig` object step by step
- `AppConfigDirector` is the director that knows the standard build order for `build_local_config()` and `build_production_config()`
- the client uses the same builder to create two ready-to-use `AppConfig` objects for different environments, while the director starts each build from a fresh config

Advantages:

- keeps many configuration steps out of one large constructor
- makes local and production setup reusable and easy to read
- lets you create partially or fully configured objects in a controlled order

Disadvantages:

- adds extra classes for a small example
- can feel verbose if the object has only a few fields

When to use:

- when one object has many optional or environment-specific settings
- when object creation should happen in a clear sequence
- when you want reusable recipes for different configurations of the same product

Reference:

- https://refactoring.guru/design-patterns/builder
