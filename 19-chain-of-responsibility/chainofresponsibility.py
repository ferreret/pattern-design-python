from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next=None):
        self._next = next

    @abstractmethod
    def handle(self, request):
        pass


class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Se ejecuta A")
        elif self._next:
            print("Se pasa al siguiente")
            self._next.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Se ejecuta B")
        elif self._next:
            print("Se pasa al siguiente")
            self._next.handle(request)


class ConcreteHandlerDefault(Handler):
    def handle(self, request):
        print("Se ejecuta por defecto")


concreteHandlerDefault = ConcreteHandlerDefault()
concreteHandlerB = ConcreteHandlerB(concreteHandlerDefault)

chain = ConcreteHandlerA(concreteHandlerB)

# chain.handle("A")
chain.handle("B")
# chain.handle("C")
