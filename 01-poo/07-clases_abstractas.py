from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def get_quantity():
        pass


# beer = (
#    Drink()
# )  # This will raise an error because we cannot instantiate an abstract class
# TypeError: Can't instantiate abstract class Drink with abstract methods get_quantity
# To fix this, we need to create a subclass that implements the abstract method.


class Beer(Drink):
    def __init__(self, quantity: int):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity


beer = Beer(10)
print(beer.get_quantity())  # Output: 10
