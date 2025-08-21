from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from typing import Any

class Mediator(ABC):
    @abstractmethod
    def notify(self, message: str, sender: object):
        pass

class Log:
    def __init__(self, log_file: str):
        self._log_file = log_file
        self._mediator = None
    
    def set_mediator(self, mediator: 'Mediator'):
        self._mediator = mediator
    
    def send(self, message: str):
        print(f"Log: {message}")
        # This line causes infinite recursion - commented out
        # self._mediator.notify(message, self)
    
    def receive(self, message: str):
        with open(self._log_file, "a") as f:
            f.write(message + "\n")

class ChatMediator(Mediator):
    def __init__(self, log: Log):
        self._users = []
        self._log = log
        self._log.set_mediator(self)
    
    def add_user(self, user):
        self._users.append(user)
    
    def notify(self, message:str, sender: object):
        self._log.send(message)
        for user in self._users:
            if user != sender:
                user.receive(message)

class User:
    def __init__(self, name: str, mediator: Mediator = None):
        self._name = name
        self._mediator = mediator
        if mediator:
            mediator.add_user(self)
    
    def send(self, message: str):
        print(f"{self._name} sent: {message}")
        self._mediator.notify(message, self)
    
    def receive(self, message: str):
        print(f"{self._name} received: {message}")

if __name__ == "__main__":
    log = Log("chat.log")
    mediator = ChatMediator(log)
    user1 = User("User1", mediator)
    user2 = User("User2", mediator)
    user3 = User("User3", mediator)

    user1.send("Hello, User2!")
    user2.send("Hi, User1!")



