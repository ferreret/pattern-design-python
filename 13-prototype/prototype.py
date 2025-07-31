"""
El patrón de diseño Prototype es un patrón creacional que permite crear nuevos
objetos duplicando una instancia existente, conocida como prototipo.

En lugar de construir un objeto desde cero, lo que puede ser costoso si la
inicialización es compleja, este patrón clona un objeto ya configurado. La idea
principal es tener un objeto prototipo y, cada vez que se necesite un nuevo
objeto similar, simplemente se copia el prototipo.

Este enfoque es útil cuando:
1.  La creación de un objeto es más costosa que su clonación.
2.  Se quiere evitar la creación de una jerarquía de fábricas paralelas a la
    jerarquía de productos (como en Abstract Factory).
3.  Las clases a instanciar se especifican en tiempo de ejecución.

En este ejemplo, la clase `Beer` actúa como un prototipo. El método `clone`
utiliza `copy.deepcopy` para crear una copia completa e independiente del objeto,
incluyendo sus atributos mutables como la lista de tamaños. Esto asegura que
las modificaciones en el clon no afecten al objeto original.
"""
from abc import ABC, abstractmethod
import copy
from typing import Self


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        pass


class Beer(Prototype):
    def __init__(self, name, brand, sizes):
        self.name = name
        self.brand = brand
        self.sizes = sizes

    def clone(self) -> Self:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"Nombre: {self.name}, Marca: {self.brand}, Tamaños: {self.sizes}"


beer = Beer("Pikantus", "Erdinger", [1000, 5000])
print(beer)

beer2 = beer.clone()
beer2.name = "Pikantus2"
beer2.sizes.append(330)

print(beer2)
print(beer)
