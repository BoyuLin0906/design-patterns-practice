# Chain of Responsibility Pattern Practice

This folder shows a simple Chain of Responsibility pattern example.

Chain of Responsibility is a behavioral design pattern that passes a request through a sequence of handlers, where each handler decides whether to process it and whether to pass it along.

Files:

- `example.py`: a number validation flow with reusable validator chains
- `README.md`: short notes for this pattern

Example:

- `ValidationHandler` is the handler interface and shared base class
- `CheckIntHandler`, `CheckPositiveHandler`, and `CheckEvenNumberHandler` are the concrete handlers
- `build_full_validation_chain` creates `check_int -> check_positive -> check_even_number`
- `build_even_only_chain` creates `check_int -> check_even_number`
- `run_validation` shows how the same request moves through different chains

Advantages:

- lets you change validation order without changing client code
- keeps each validation rule small and focused
- makes it easy to reuse handlers in different combinations

Disadvantages:

- adds extra classes for a small validation task
- tracing the request can be harder if the chain becomes long
- some requests may stop early or reach the end without full handling

When to use:

- when a request should go through several checks in order
- when you want to reuse the same handlers in different combinations
- when you want to add or remove steps without rewriting the whole flow

Reference:

- https://refactoring.guru/design-patterns/chain-of-responsibility
