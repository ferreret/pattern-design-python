from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """
    Abstract base class for observers in the observer pattern.
    Observers must implement the update method to receive notifications.
    """

    @abstractmethod
    def refresh(self, subject):
        pass


class Subject:
    """
    Subject class that maintains a list of observers and notifies them of changes.
    Observers can subscribe or unsubscribe to the subject.
    """

    def __init__(self):
        self._observers: List[Observer] = []

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
        Notify all subscribed observers with the current state of the subject.
        """
        for observer in self._observers:
            observer.refresh(self)


class System(Subject):
    """
    Concrete subject that extends the Subject class.
    It can have its own state and notify observers about changes.
    """

    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class FileObserver(Observer):
    """
    Concrete observer that implements the Observer interface.
    Writes notifications to a file.
    """

    def __init__(self, filename):
        self.filename = filename

    def refresh(self, subject):
        with open(self.filename, "a") as file:
            file.write(f"State changed to: {subject.state}\n")


class ConsoleObserver(Observer):
    """
    Concrete observer that implements the Observer interface.
    Prints notifications to the console.
    """

    def refresh(self, subject):
        print(f"ConsoleObserver: State changed to {subject.state}")


file_observer = FileObserver("log.txt")
console_observer = ConsoleObserver()

system = System()
system.subscribe(file_observer)
system.subscribe(console_observer)
system.state = "Activo"
system.state = "Inactivo"

system.unsubscribe(file_observer)
system.state = "Activo"
