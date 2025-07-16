from abc import ABC, abstractmethod


class Concept(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class Product(Concept):
    def __init__(self, amount, tax) -> None:
        self._amount = amount
        self._tax = tax

    def price(self) -> float:
        return self._amount + self._tax

    def description(
        self,
    ) -> str:
        return "This is a product."


class Service(Concept):
    def __init__(self, amount) -> None:
        self._amount = amount

    def price(self) -> float:
        return self._amount

    def description(self) -> str:
        return "This is a service."


class ConceptFactory(ABC):
    def __init__(self, *args) -> None:
        self._args = args

    @abstractmethod
    def create(self) -> Concept:
        pass


class ProductFactory(ConceptFactory):
    def create(self) -> Concept:
        return Product(self._args[0], self._args[1])


class ServiceFactory(ConceptFactory):
    def create(self) -> Concept:
        return Service(self._args[0])


def show_info(concept: Concept) -> None:
    print("El concepto es:", concept.description())


product_factory = ProductFactory(40, 10)
service_factory = ServiceFactory(20)

concept1 = product_factory.create()
concept2 = service_factory.create()


show_info(concept1)
show_info(concept2)

print("Precio del producto:", concept1.price())
print("Precio del servicio:", concept2.price())
# Output:
# El concepto es: This is a product.
# El concepto es: This is a service.
# Precio del producto: 50
# Precio del servicio: 20
# This code demonstrates the Factory Method pattern with an added state (price) for each concept (Product and Service).
# The Concept class now includes a price method, and both Product and Service implement this method.
# The factories are modified to accept parameters necessary for creating instances of Product and Service.
# The show_info function displays the description of each concept, while the price of each concept is printed separately.
# This allows for easy extension and modification of concept types without changing the client code,
# adhering to the Open/Closed Principle while also managing state effectively.
# This pattern is useful in scenarios where the system needs to be independent of how its objects are created,
# composed, and represented, promoting flexibility and scalability in the codebase.
