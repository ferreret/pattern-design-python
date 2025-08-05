# Patrón de diseño de tipo estructural

# Este patrón permite que clases que no siguen la estructura de las que están en funciomaniento,
# permitan modificarlas para que sigan el diseño.

from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def payment(self, amount: float):
        pass


class Adaptee:
    def __init__(self):
        self.__connected = False

    def connect(self):
        print("Conectando")
        self.__connected = True

    def pay(self, amount: float):
        if self.__connected:
            print("Realizamos el pago")


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
        self.adaptee.connect()

    def payment(self, amount: float):
        self.adaptee.pay(amount)


def create_order(pay: Target, amount: float):
    pay.payment(amount)
    print("Se factura")
    print("Se envia la factura por email")


adaptee = Adaptee()
adapter = Adapter(adaptee)
create_order(adapter, 100)
