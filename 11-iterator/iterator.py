# El patrón de diseño Iterator permite recorrer una colección de objetos sin exponer su representación interna.
# Este código define las interfaces y clases necesarias para implementar un iterador concreto.


from abc import ABC, abstractmethod
from typing import Any, List


class Iterator(ABC):
    @abstractmethod
    def next(self) -> Any:
        """Return the next item in the collection."""
        pass

    @abstractmethod
    def has_next(self) -> bool:
        """Return True if there are more items in the collection."""
        pass


class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        """Return an iterator for the collection."""
        pass


class ConcreteCollection(IterableCollection):
    def __init__(self, items: List[Any]):
        self._items = items

    def create_iterator(self) -> Iterator:
        return ConcreteIterator(self)

    def get_items(self) -> List[Any]:
        return self._items


class ConcreteIterator(Iterator):
    def __init__(self, collection: ConcreteCollection):
        self._collection = collection
        self._index = 0

    def next(self) -> Any:
        if self.has_next():
            item = self._collection.get_items()[self._index]
            self._index += 1
            return item

    def has_next(self) -> bool:
        return self._index < len(self._collection.get_items())


# Ejemplo de uso
collection = ConcreteCollection(["a", "b", "c"])
iterator = collection.create_iterator()

while iterator.has_next():
    print(iterator.next())
# Salida esperada:
# a
# b
# c
# El iterador permite recorrer la colección sin exponer su estructura interna.
# Esto es útil para mantener la encapsulación y la separación de preocupaciones.
# Además, se puede cambiar la implementación del iterador sin afectar al cliente que lo utiliza.
# Este patrón es especialmente útil cuando se trabaja con colecciones complejas o grandes,
# ya que permite una navegación eficiente y controlada a través de los elementos.
