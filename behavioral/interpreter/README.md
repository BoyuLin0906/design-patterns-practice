# Interpreter Pattern Practice

This folder shows a simple Interpreter pattern example.

Interpreter is a behavioral design pattern that defines a small language, represents its grammar with classes, and evaluates sentences by calling `interpret()` on those objects.

Files:

- `behavioral/interpreter/example.py`: a person rule checker built from small expression objects
- `behavioral/interpreter/README.md`: short notes for this pattern

Example:

- `PersonExpression` is the shared interpreter interface
- `CountryIs` and `AgeAtLeast` are terminal expressions
- `AndExpression` is the non-terminal expression that combines other rules
- `PersonContext` is the context object that stores the current input data and an evaluation trace
- `PersonRuleChecker` is the coordinating object that runs the root rule against a `PersonContext`
- the example builds the rule `country is TW AND age is at least 18` and interprets it for different people

Advantages:

- keeps each grammar rule in its own class
- makes a small domain language easy to read and extend
- fits naturally when rules can be represented as a tree

Disadvantages:

- adds many classes for even a small grammar
- can become hard to manage when the language grows
- does not solve parsing by itself

When to use:

- when you have a small, repeated rule language in one domain
- when the rules can be modeled as terminal and non-terminal expressions
- when you want to evaluate combinations of rules without large condition blocks

Reference:

- https://sourcemaking.com/design_patterns/interpreter
