# Adapter Pattern Practice

This folder shows a simple Adapter pattern example.

Adapter is a structural design pattern that lets objects with incompatible interfaces work together by converting one interface into another that the client can use.

This example uses the object adapter style, where each adapter wraps an existing notifier through composition.

Files:

- `structural/adapter/example.py`: a notification example that sends messages through email, Slack, and app adapters
- `structural/adapter/README.md`: short notes for this pattern

Example:

- `NotificationChannel` is the target interface the client understands
- `EmailNotifier`, `SlackNotifier`, and `AppNotifier` are existing services with different method names and parameter shapes
- `EmailAdapter`, `SlackAdapter`, and `AppAdapter` convert those services into the shared `send()` interface
- `deliver_notification()` is the client code and works with all channels in the same way because it only depends on the adapter interface

Advantages:

- lets you reuse existing classes without changing their original interface
- keeps conversion logic separate from the main sending flow
- makes it easy to add another notification platform later

Disadvantages:

- adds extra classes and one more layer of indirection
- can feel unnecessary if the interfaces are already very similar

When to use:

- when you need to integrate an existing class but its interface does not match your current code
- when several services do similar work but expose different APIs
- when you want client code to depend on one stable interface

Reference:

- https://refactoring.guru/design-patterns/adapter
