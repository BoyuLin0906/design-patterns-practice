# Flyweight Pattern Practice

Flyweight is a structural design pattern that saves memory by sharing common state between many similar objects.

Files:

- `structural/flyweight/example.py`: a forest example where many `Tree` objects reuse shared tree type data
- `structural/flyweight/README.md`: short notes for this pattern

Example:

- `TreeType` is the flyweight and stores the intrinsic state: `name` and `texture`
- `Tree` is the context object and stores the extrinsic state: `x` and `y`
- `TreeFactory` manages a pool of shared `TreeType` objects and returns an existing one when the same intrinsic state is requested
- `Forest` plants many trees and reuses the same `TreeType` for matching tree data
- the main block plants several trees, draws them, and shows that repeated tree types are shared

Advantages:

- reduces repeated data when many objects share the same intrinsic state
- keeps the shared state in one place through `TreeFactory`
- makes object reuse easy to see in a tree or map style example

Disadvantages:

- separates object state into intrinsic and extrinsic parts, which adds indirection
- can make the code harder to follow if there are only a few objects
- may add lookup overhead when retrieving shared flyweights

When to use:

- when you need a large number of similar objects in memory at the same time
- when many of those objects share the same unchanging data
- when the unique context can be passed in separately or stored in a lightweight object

Reference:

- https://refactoring.guru/design-patterns/flyweight
