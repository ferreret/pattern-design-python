from abc import ABC, abstractmethod


class OrderState(ABC):
    """
    Abstract base class for an order state in a state machine.
    """

    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def ship(self, order):
        pass

    @abstractmethod
    def deliver(self, order):
        pass


class NewOrderState(OrderState):
    def pay(self, order):
        print("Payment received. Transitioning to Processing state.")
        order.set_state(PaidOrderState())

    def ship(self, order):
        print("Cannot ship. Order is still new and not paid.")

    def deliver(self, order):
        print("Cannot deliver. Order is still new and not paid.")


class PaidOrderState(OrderState):
    def pay(self, order):
        print("Order already paid. No action taken.")

    def ship(self, order):
        print("Order shipped. Transitioning to Shipped state.")
        order.set_state(ShippedOrderState())

    def deliver(self, order):
        print("Cannot deliver. Order is still in processing.")


class ShippedOrderState(OrderState):
    def pay(self, order):
        print("Order already paid. No action taken.")

    def ship(self, order):
        print("Order already shipped. No action taken.")

    def deliver(self, order):
        print("Order delivered. Transitioning to Delivered state.")
        order.set_state(DeliveredOrderState())


class DeliveredOrderState(OrderState):
    def pay(self, order):
        print("Order already paid. No action taken.")

    def ship(self, order):
        print("Order already delivered. No action taken.")

    def deliver(self, order):
        print("Order already delivered. No action taken.")


class Order:
    def __init__(self, state: OrderState):
        self._state = state

    def set_state(self, state: OrderState) -> None:
        self._state = state

    def pay(self) -> None:
        self._state.pay(self)

    def ship(self) -> None:
        self._state.ship(self)

    def deliver(self) -> None:
        self._state.deliver(self)


order = Order(NewOrderState())

# Example usage
order.ship()  # Cannot ship, order is new
order.pay()  # Payment received, transitioning to Paid state
order.ship()  # Order shipped, transitioning to Shipped state
order.deliver()  # Order delivered, transitioning to Delivered state
order.pay()  # No action taken, order already paid
order.ship()  # No action taken, order already shipped
order.deliver()  # No action taken, order already delivered
