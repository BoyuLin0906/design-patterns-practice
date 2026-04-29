from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start, destination):
        pass


class WalkingStrategy(RouteStrategy):
    def build_route(self, start, destination):
        return {
            'mode': 'walking',
            'eta_minutes': 30,
            'steps': [
                f'Walk from {start}.',
                'Use the sidewalk.',
                f'Arrive at {destination}.',
            ],
        }


class DrivingStrategy(RouteStrategy):
    def build_route(self, start, destination):
        return {
            'mode': 'driving',
            'eta_minutes': 12,
            'steps': [
                f'Drive from {start}.',
                'Take the main road.',
                f'Park near {destination}.',
            ],
        }


class PublicTransportStrategy(RouteStrategy):
    def build_route(self, start, destination):
        return {
            'mode': 'public transport',
            'eta_minutes': 20,
            'steps': [
                f'Walk from {start} to the bus stop.',
                'Take bus 21.',
                f'Get off near {destination}.',
            ],
        }


class Navigator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def build_route(self, start, destination):
        return self.strategy.build_route(start, destination)


def print_route(route):
    print(f'Mode: {route["mode"]}')
    print(f'ETA: {route["eta_minutes"]} minutes')
    print('Steps:')
    for step in route['steps']:
        print(f'- {step}')
    print()


if __name__ == '__main__':
    navigator = Navigator(WalkingStrategy())

    print_section('Walking Route')
    route = navigator.build_route('Home', 'Office')
    print_route(route)

    navigator.set_strategy(DrivingStrategy())
    print_section('Driving Route')
    route = navigator.build_route('Home', 'Office')
    print_route(route)

    navigator.set_strategy(PublicTransportStrategy())
    print_section('Public Transport Route')
    route = navigator.build_route('Home', 'Office')
    print_route(route)
