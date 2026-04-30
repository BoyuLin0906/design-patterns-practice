# Bridge Pattern Practice

This folder shows a simple Bridge pattern example.

Bridge is a structural design pattern that splits one concept into two independent hierarchies so both sides can vary without creating a class for every combination.

Files:

- `structural/bridge/example.py`: a notification example with message types and delivery channels
- `structural/bridge/README.md`: short notes for this pattern

Example:

- `MessageSender` is the implementation interface for delivery platforms
- `EmailSender` and `SlackSender` are the concrete implementations
- `NotificationMessage` is the abstraction that delegates delivery to a sender
- `AlertNotification` and `ReminderNotification` are refined abstractions with different message formatting rules
- the client can combine any notification type with any sender, such as `AlertNotification(EmailSender())` or `ReminderNotification(SlackSender())`

Advantages:

- avoids creating a separate class for every notification-type and sender combination
- lets you add a new sender without changing the notification hierarchy
- lets you add a new notification style without changing the sender hierarchy

Disadvantages:

- adds more classes and indirection for a small example
- can feel unnecessary when there is only one changing dimension

When to use:

- when a class needs to vary in two independent dimensions
- when subclass combinations would otherwise grow quickly
- when you want high-level logic and platform-specific behavior to evolve separately

Reference:

- https://refactoring.guru/design-patterns/bridge
