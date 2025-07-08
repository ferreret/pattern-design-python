from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def get_quantity(self):
        pass

    def description(self):
        """A method that can be overridden by subclasses to provide a description."""
        print("This is a drink.")


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

beer.description()  # Output: This is a drink.
# You can also override the description method in the Beer class if needed.
# For example:
# class Beer(Drink):
#     def __init__(self, quantity: int):
#         self.__quantity = quantity
#
#     def get_quantity(self):
#         return self.__quantity
#
#     def description(self):
#         print("This is a beer drink.")
# beer = Beer(10)
# beer.description()  # Output: This is a beer drink.
# This way, you can provide a specific description for the Beer class while still adhering to the abstract base class structure.
