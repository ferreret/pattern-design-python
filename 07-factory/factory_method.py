from abc import ABC, abstractmethod


class Concept(ABC):
    @abstractmethod
    def description(self) -> str:
        pass


class Product(Concept):
    def description(self) -> str:
        return "This is a product."


class Service(Concept):
    def description(self) -> str:
        return "This is a service."


class ConceptFactory(ABC):
    @abstractmethod
    def create(self) -> Concept:
        pass


class ProductFactory(ConceptFactory):
    def create(self) -> Concept:
        return Product()


class ServiceFactory(ConceptFactory):
    def create(self) -> Concept:
        return Service()


def show_info(concept: Concept) -> None:
    print("El concepto es:", concept.description())


product_factory = ProductFactory()
service_factory = ServiceFactory()

concept1 = product_factory.create()
concept2 = service_factory.create()


show_info(concept1)
show_info(concept2)
# Output:
# El concepto es: This is a product.
# El concepto es: This is a service.
# This code demonstrates the Factory Method pattern by creating different types of concepts (Product and Service)
# using their respective factories. The show_info function displays the description of each concept.
# This allows for easy extension and modification of concept types without changing the client code.
# The factories encapsulate the creation logic, adhering to the Open/Closed Principle.
# This pattern is useful in scenarios where the system needs to be independent of how its objects are created,
# composed, and represented, promoting flexibility and scalability in the codebase.
