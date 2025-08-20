# Patrón de diseño de tipo de comportamiento.

from abc import ABC, abstractmethod

class Receiver:
    def open(self):
        print("Abrir el archivo")
    def save(self):
        print("Guardar el archivo")
    def print(self):
        print("Imprimir el archivo")

class Command(ABC):
    def __init__(self, receiver: Receiver) -> None:
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass

class OpenCommand(Command):
    def execute(self):
        self._receiver.open()

class SaveCommand(Command):
    def execute(self):
        self._receiver.save()

class PrintCommand(Command):
    def execute(self):
        self._receiver.print()

# La clase Invoker está desacoplada de Receiver, se puede modificar Receiver sin tener que modificar el Invoker.
class Invoker:
    def __init__(self, open: Command, save: Command, print: Command) -> None:
        self._open = open
        self._save = save
        self._print = print

    def open(self):
        self._open.execute()

    def save(self):
        self._save.execute()

    def print(self):
        self._print.execute()


receiver = Receiver()
open_command = OpenCommand(receiver)
save_command = SaveCommand(receiver)
print_command = PrintCommand(receiver)
invoker = Invoker(open_command, save_command, print_command)
invoker.open()
invoker.save()
invoker.print()



