# El patrón strategy es de tipo comportamiento.
# Se utilizan interfaces para definir un conjunto de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables.
# En python se puede implementar de varias maneras, pero una forma común es usar clases abstractas o interfaces.

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b


class MultiplyStrategy(Strategy):
    def execute(self, a, b):
        return a * b


# Es la clase que utiliza la estrategia y es la clase de contexto
class Operation:
    def __init__(self, strategy: Strategy):
        self.__strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.__strategy = strategy

    def execute(self, a, b):
        return self.__strategy.execute(a, b)


add_strategy = AddStrategy()
mult_strategy = MultiplyStrategy()

operation = Operation(add_strategy)

print(operation.execute(5, 3))  # Salida: 8

operation.set_strategy(mult_strategy)
print(operation.execute(5, 3))  # Salida: 15
