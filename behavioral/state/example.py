from __future__ import annotations

from abc import ABC, abstractmethod


def print_section(title):
    print(f'\n=== {title} ===')


class OrderState(ABC):
    @abstractmethod
    def pay(self, order: ShoppingOrderContext):
        raise NotImplementedError('Subclasses must implement pay().')

    @abstractmethod
    def ship(self, order: ShoppingOrderContext):
        raise NotImplementedError('Subclasses must implement ship().')

    @abstractmethod
    def label(self):
        raise NotImplementedError('Subclasses must implement label().')


class OrderRepository:
    def __init__(self):
        self._orders = {}

    def save_state(self, order_id, customer_name, state_name):
        self._orders[order_id] = {
            'order_id': order_id,
            'customer_name': customer_name,
            'state': state_name,
        }
        print(f'DB update: order #{order_id} saved as {state_name}.')

    def display(self):
        print_section('Fake Database')
        for order in self._orders.values():
            print(
                f'order_id={order["order_id"]} | '
                f'customer_name={order["customer_name"]} | '
                f'state={order["state"]}'
            )


class CreatedState(OrderState):
    def pay(self, order: ShoppingOrderContext):
        print(f'Order #{order.order_id}: payment accepted.')
        order.transition_to(PaidState())

    def ship(self, order: ShoppingOrderContext):
        print(f'Order #{order.order_id}: cannot ship before payment.')

    def label(self):
        return 'created'


class PaidState(OrderState):
    def pay(self, order: ShoppingOrderContext):
        print(f'Order #{order.order_id}: payment was already completed.')

    def ship(self, order: ShoppingOrderContext):
        print(f'Order #{order.order_id}: shipment started.')
        order.transition_to(ShippedState())

    def label(self):
        return 'paid'


class ShippedState(OrderState):
    def pay(self, order: ShoppingOrderContext):
        print(f'Order #{order.order_id}: payment is already closed after shipping.')

    def ship(self, order: ShoppingOrderContext):
        print(f'Order #{order.order_id}: order was already shipped.')

    def label(self):
        return 'shipped'


class ShoppingOrderContext:
    def __init__(
        self,
        repository: OrderRepository,
        order_id,
        customer_name,
    ):
        self.order_id = order_id
        self.customer_name = customer_name
        self.repository: OrderRepository = repository
        self.state: OrderState = CreatedState()
        self.repository.save_state(self.order_id, self.customer_name, self.state.label())

    def transition_to(self, state: OrderState):
        previous_state = self.state.label()
        self.state = state
        self.repository.save_state(self.order_id, self.customer_name, self.state.label())
        print(f'state changed: {previous_state} -> {self.state.label()}')

    def pay(self):
        self.state.pay(self)

    def ship(self):
        self.state.ship(self)

    def show_status(self):
        print(
            f'Order #{self.order_id} for {self.customer_name} '
            f'is currently {self.state.label()}.'
        )


if __name__ == '__main__':
    repository = OrderRepository()
    order = ShoppingOrderContext(
        repository=repository,
        order_id=501,
        customer_name='Andy Lin',
    )

    print_section('Initial State')
    order.show_status()

    print_section('Try To Ship Too Early')
    order.ship()
    order.show_status()

    print_section('Pay Order')
    order.pay()
    order.show_status()

    print_section('Ship Order')
    order.ship()
    order.show_status()

    print_section('Repeat Actions After Shipping')
    order.pay()
    order.ship()

    repository.display()
