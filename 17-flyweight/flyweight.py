# Patrón de tipo estructural, que sirve para optimizar la memoria
from abc import ABC, abstractmethod


class Flyweight(ABC):
    @abstractmethod
    def print(self, size: int):
        pass


class ConcreteFlyweight(Flyweight):
    def __init__(self, char: str):
        self.__char = char  # estado compartido

    def print(self, size: int):  # no compartido
        print(f"Letra {self.__char} de tamaño {size}")


class FlyweightFactory:
    def __init__(self):
        self.__chars = {}

    def get(self, char: str) -> Flyweight:
        if char not in self.__chars:
            print(f"Creando letra {char}")
            self.__chars[char] = ConcreteFlyweight(char)
        return self.__chars[char]


flyweight_factory = FlyweightFactory()

a1 = flyweight_factory.get("a")
a1.print(11)

a2 = flyweight_factory.get("a")
a2.print(12)

b1 = flyweight_factory.get("b")
b1.print(21)
