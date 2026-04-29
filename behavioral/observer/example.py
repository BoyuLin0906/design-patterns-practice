from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class EventListener(ABC):
    @abstractmethod
    def update(self, event_type, data):
        pass


class SlackListener(EventListener):
    def update(self, event_type, data):
        print(f'[Slack] {event_type}: {data}')


class EmailListener(EventListener):
    def update(self, event_type, data):
        print(f'[Email] {event_type}: {data}')


class MobileListener(EventListener):
    def update(self, event_type, data):
        print(f'[Mobile] {event_type}: {data}')


class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        self.listeners.setdefault(event_type, []).append(listener)

    def unsubscribe(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        for listener in self.listeners.get(event_type, []):
            listener.update(event_type, data)


if __name__ == '__main__':
    event_manager = EventManager()

    slack_listener = SlackListener()
    email_listener = EmailListener()
    mobile_listener = MobileListener()

    event_manager.subscribe('deploy', slack_listener)
    event_manager.subscribe('deploy', email_listener)
    event_manager.subscribe('alert', mobile_listener)
    event_manager.subscribe('alert', slack_listener)

    print_section('Send Deploy Event')
    event_manager.notify('deploy', 'Version 1.2.0 is deployed.')

    print_section('Send Alert Event')
    event_manager.notify('alert', 'CPU usage is above 90%.')

    event_manager.unsubscribe('alert', slack_listener)

    print_section('Send Alert Event Again')
    event_manager.notify('alert', 'Disk space is below 10%.')
