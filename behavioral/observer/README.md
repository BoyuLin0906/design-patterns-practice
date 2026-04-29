# Observer Pattern Practice

This folder shows a simple Observer pattern example.

Observer is a behavioral design pattern that lets objects subscribe to events and receive updates when something important happens in the publisher.

Files:

- `example.py`: an `EventManager` publisher with Slack, Email, and Mobile listeners
- `README.md`: short notes for this pattern

Example:

- `EventManager` is the publisher
- `SlackListener`, `EmailListener`, and `MobileListener` are the subscribers
- listeners can subscribe, unsubscribe, and react when an event is published

Advantages:

- adds new listeners without changing the publisher
- supports runtime subscribe and unsubscribe behavior
- keeps notification handling separate from event publishing

Disadvantages:

- subscribers are notified in list order
- too many subscriptions can make event flow harder to follow

When to use:

- when one object needs to notify many other objects about events
- when subscribers may join or leave dynamically
- when you want to reduce direct coupling between the publisher and receivers

Extension idea:

- First-level Observer: publisher = YouTube, subscribers = audience.
  - Flow: YouTube publishes a new video, and the audience receives the event.
- Second-level Observer: publisher = audience, subscribers = email, app, and mobile channels.
  - Flow: the audience receives the event, then notifies email, app, and mobile channels.

Reference:

- https://refactoring.guru/design-patterns/observer
