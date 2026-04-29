# Mediator Pattern Practice

Mediator is a behavioral design pattern that centralizes how related objects collaborate so they do not call each other directly.

Files:

- `behavioral/mediator/example.py`: a simple chat room workflow coordinated by a mediator
- `behavioral/mediator/README.md`: short notes for this pattern

Example:

- `ChatComponent` is the shared abstraction for chat participants
- `ChatRoomMediator` is the mediator that decides how messages are delivered
- `UserComponent` and `BotComponent` are chat components that know only the mediator
- `UserComponent.send()` sends a message through the mediator instead of calling other participants directly
- `BotComponent.receive()` replies only when its name is mentioned and the message contains `help`
- `ChatRoomMediator.notify()` forwards each message to every registered component except the sender
- the main block shows a regular message and a help request that mentions `HelperBot`

Advantages:

- keeps message routing in one place
- reduces direct coupling between chat participants
- makes `UserComponent` and `BotComponent` easier to change independently

Disadvantages:

- the mediator can grow too large if too much logic is moved into it
- adds extra structure for a small chat flow
- very small programs may not need this pattern

When to use:

- when classes are hard to change because they are tightly coupled to many other classes
- when a component is hard to reuse because it depends on too many collaborators
- when you want to change how components collaborate without changing the components themselves

Reference:

- https://refactoring.guru/design-patterns/mediator
