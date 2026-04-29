from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class ChatComponent(ABC):
    def __init__(self, mediator: ChatRoomMediator, name):
        self.mediator: ChatRoomMediator = mediator
        self.name = name

    def send(self, message):
        print(f'{self.name} sends: {message}')
        self.mediator.notify(self, message)

    @abstractmethod
    def receive(self, sender, message):
        raise NotImplementedError('Subclasses must implement receive().')


class UserComponent(ChatComponent):
    def receive(self, sender, message):
        print(f'{self.name} receives from {sender.name}: {message}')


class BotComponent(ChatComponent):
    def receive(self, sender, message):
        print(f'{self.name} notices {sender.name} said: {message}')

        if isinstance(sender, BotComponent):
            return

        lowered_message = message.lower()
        mentioned = self.name.lower() in lowered_message
        needs_help = 'help' in lowered_message

        if mentioned and needs_help:
            self.send(f'{sender.name}, what can I help you with?')


class ChatRoomMediator:
    def __init__(self):
        self.components = []

    def register(self, component):
        self.components.append(component)
        print(f'ChatRoomMediator: registered {component.name}.')

    def notify(self, sender, message):
        print(f'ChatRoomMediator: delivering message from {sender.name}.')
        for component in self.components:
            if component is not sender:
                component.receive(sender, message)


if __name__ == '__main__':
    chat_mediator = ChatRoomMediator()

    alice = UserComponent(chat_mediator, 'Alice')
    bob = UserComponent(chat_mediator, 'Bob')
    helper_bot = BotComponent(chat_mediator, 'HelperBot')

    print_section('Register Components')
    chat_mediator.register(alice)
    chat_mediator.register(bob)
    chat_mediator.register(helper_bot)

    print_section('Regular Message')
    alice.send('Hello everyone!')

    print_section('Ask Bot For Help')
    bob.send('HelperBot, can you help me with the payment page?')
