from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """
    Abstract base class for observers in the observer pattern.
    Observers must implement the update method to receive notifications.
    """

    @abstractmethod
    def refresh(self, ticket_number):
        pass


class Subject:
    """
    Subject class that maintains a list of observers and notifies them of changes.
    Observers can subscribe or unsubscribe to the subject.
    """

    def __init__(self):
        self._observers: List[Observer] = []
        self._tickets = 1

    def subscribe(self, observer: Observer):
        """
        Subscribe an observer to the subject.
        :param observer: An instance of Observer to be added.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        """
        Unsubscribe an observer from the subject.
        :param observer: An instance of Observer to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        """
        Notify all subscribed observers with the current ticket number.
        """
        for observer in self._observers:
            observer.refresh(self._tickets)

    def sell(self):
        """
        Simulate selling a ticket and notify all observers.
        Increments the ticket number and calls notify.
        """
        self.notify()
        self._tickets += 1


class SendMail(Observer):
    """
    Concrete observer that implements the Observer interface.
    Sends an email notification with the ticket number.
    """

    def refresh(self, ticket_number):
        print(f"SendMail: Ticket number {ticket_number} has been sold.")


class Invoice(Observer):
    """
    Concrete observer that implements the Observer interface.
    Generates an invoice notification with the ticket number.
    """

    def refresh(self, ticket_number):
        print(f"Invoice: Generating invoice for ticket number {ticket_number}.")


send_mail = SendMail()
invoice = Invoice()

subject = Subject()
subject.subscribe(send_mail)
subject.subscribe(invoice)

subject.sell()
subject.sell()
subject.sell()

subject.unsubscribe(send_mail)

subject.sell()
subject.sell()
subject.sell()
