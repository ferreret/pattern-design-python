# Es un patrón de diseño estructural que permite que dos clases trabajen juntas,
# incluso si no tienen interfaces compatibles.
# El patrón Bridge separa la abstracción de su implementación para que ambas puedan variar independientemente.

from abc import ABC, abstractmethod


class Implementor(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass


class AddCalculation(Implementor):
    def calculate(self, a: float, b: float) -> float:
        return a + b


class MultiplyCalculation(Implementor):
    def calculate(self, a: float, b: float) -> float:
        return a * b


class Abstraction(ABC):
    def __init__(self, calculation: Implementor, numbers):
        self.calculation = calculation
        self.numbers = numbers

    @abstractmethod
    def print(self, n: float) -> None:
        pass


class Numbers(Abstraction):
    def print(self, n: float) -> None:
        for number in self.numbers:
            print(
                f"{self.calculation.calculate(n, number)}"
            )  # Suma cada número de la lista a n


add = AddCalculation()
multiply = MultiplyCalculation()

numbers = Numbers(add, [1, 2, 3])
numbers.print(2)

numbers2 = Numbers(multiply, [1, 2, 3])
numbers2.print(2)  # Multiplica cada número de la lista por n
# Output:
# 3.0
# 4.0
# 5.0
