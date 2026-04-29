# Strategy Pattern Practice

This folder shows a simple Strategy pattern example.

Strategy is a behavioral design pattern that puts different versions of the same behavior into separate classes and makes them interchangeable. The main object delegates the work to the selected strategy.

Files:

- `example.py`: a navigator that can build routes by walking, driving, or public transport
- `README.md`: short notes for this pattern

Example:

- `Navigator` is the context
- `WalkingStrategy`, `DrivingStrategy`, and `PublicTransportStrategy` are the strategies
- the navigator can switch strategies without changing its own route-building logic

Advantages:

- lets you swap algorithms at runtime
- keeps algorithm details separate from the code that uses them
- makes it easier to add new route types later

Disadvantages:

- adds extra classes for small problems
- the caller still needs to choose the right strategy

When to use:

- when one object needs multiple ways to perform the same task
- when you want to switch behavior at runtime
- when condition-heavy logic is becoming hard to maintain

Reference:

- https://refactoring.guru/design-patterns/strategy
