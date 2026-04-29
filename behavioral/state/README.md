# State Pattern Practice

This folder shows a simple State pattern example.

State is a behavioral design pattern that lets an object change its behavior when its internal state changes.

Files:

- `example.py`: a shopping order workflow with three order states
- `README.md`: short notes for this pattern

Example:

- `OrderState` is the shared state interface
- `OrderRepository` is a small repository that simulates saving the current order state
- `CreatedState`, `PaidState`, and `ShippedState` are the concrete states
- `ShoppingOrderContext` is the context that delegates `pay()` and `ship()` to the current state
- `ShoppingOrderContext.pay()` calls `self.state.pay(self)` and `ShoppingOrderContext.ship()` calls `self.state.ship(self)`, so each state receives the context and can change it with `transition_to`
- `ShoppingOrderContext.transition_to()` updates the in-memory state and asks `OrderRepository` to save the new state

Notes:

- This practice example keeps the flow intentionally small with `created -> paid -> shipped`
- In a more realistic order system, you might add in-progress states such as `paying` and `shipping`, with extra actions like confirming payment or completing shipment

Advantages:

- removes conditional state checks from `ShoppingOrder`
- keeps transition rules close to the state that owns them
- makes it easy to add a new order state later

Disadvantages:

- adds extra classes for a very small workflow
- transitions can become harder to trace when many states are added
- some simple state machines may not need this pattern

When to use:

- when an object should react differently depending on its current state
- when state transitions are clear and likely to grow over time
- when you want to replace large `if` or `match` blocks with dedicated classes

Reference:

- https://refactoring.guru/design-patterns/state
