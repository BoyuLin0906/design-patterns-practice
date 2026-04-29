# Command Pattern Practice

This folder shows a simple Command pattern example.

Command is a behavioral design pattern that turns a request into an object so it can be stored, executed later, and tracked in history.

Files:

- `example.py`: a fake user workflow with command objects, receivers, and command history
- `README.md`: short notes for this pattern

Example:

- `Command` is the shared command interface
- `SaveUserCommand` and `SendEmailCommand` are the concrete commands
- `FakeDatabase` and `EmailService` are the receivers that do the real work
- `CommandInvoker` is the invoker that queues commands, runs them together, and asks `CommandHistory` to record them
- `HistoryEntry` is the small record object for each executed action
- `CommandHistory` stores `HistoryEntry` records and lets `CommandInvoker.rerun` execute a specific past command again
- `UserData` carries the fake `user_id`, `user_name`, and `email` used by all commands

Advantages:

- separates the object that requests work from the objects that perform it
- makes it easy to log, store, and rerun actions
- lets you add new commands without changing the invoker

Disadvantages:

- adds more classes for a small workflow
- simple actions can feel more verbose when wrapped as command objects
- history and replay rules need care as the system grows

When to use:

- when you want to parameterize objects with operations and pass actions around as objects
- when you need to queue, log, delay, schedule, or remotely trigger operations
- when you need command history for replay, undo, redo, or other reversible behavior

Reference:

- https://refactoring.guru/design-patterns/command
