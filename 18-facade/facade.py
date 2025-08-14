# Es un patrón de diseño de tipo estructural.
# Unifica la complejidad de clases, oculta la complejidad de una librería y muestra una interfaz más sencilla.


class Stock:
    def check(self, concepts) -> bool:
        return True


class Payment:
    def pay(self, customer_id, concepts):
        print(f"Se realiza el pago")


class Email:
    def send(self, customer_id):
        print(f"Su ocompra fue hecha con éxito.")


class Facade:
    def __init__(self) -> None:
        self.__stock = Stock()
        self.__payment = Payment()
        self.__email = Email()

    # Unificamos las operaciones frecuentes en el método de la clase Facade
    def create_payment(self, concepts, customer_id):
        if self.__stock.check(concepts):
            self.__payment.pay(customer_id, concepts)
            self.__email.send(customer_id)


concepts = [
    {"id": 1, "quantity": 10},
    {"id": 2, "quantity": 20},
    {"id": 3, "quantity": 15},
]

facade = Facade()
facade.create_payment(concepts, 1)
