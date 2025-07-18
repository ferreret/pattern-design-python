# Es un patrón de diseño que es util cuando los objetos a crear son complejos
# y se requiere un proceso de construcción paso a paso.
# Permite crear un objeto complejo separando su construcción de su representación.
from abc import ABC, abstractmethod
from typing import Optional


class People:
    def __init__(self):
        self.name: Optional[str] = None
        self.age: Optional[int] = None
        self.country: Optional[str] = None
        self.weight: Optional[float] = None

    def __str__(self):
        return (
            f"People(name={self.name}, age={self.age}, "
            f"country={self.country}, weight={self.weight})"
        )


class Builder(ABC):
    @abstractmethod
    def set_name(self, name) -> "Builder":
        pass

    @abstractmethod
    def set_age(self, age) -> "Builder":
        pass

    @abstractmethod
    def set_country(self, country) -> "Builder":
        pass

    @abstractmethod
    def set_weight(self, weight) -> "Builder":
        pass

    @abstractmethod
    def build(self) -> People:
        pass


class PeopleBuilder(Builder):
    def __init__(self):
        self.__people = People()

    def set_name(self, name):
        self.__people.name = name
        return self

    def set_age(self, age: int):
        self.__people.age = age
        return self

    def set_country(self, country: str):
        self.__people.country = country
        return self

    def set_weight(self, weight: float):
        self.__people.weight = weight
        return self

    def build(self) -> People:
        people = self.__people
        self.reset()  # Reset the builder for future use
        return people

    def reset(self):
        self.__people = People()


class PeopleDirector:
    def __init__(self, builder: Builder):
        self._builder = builder

    def create_hector(self):
        self._builder.set_name("Hector").set_age(30).set_country("Colombia").set_weight(
            70.5
        )
        return self._builder.build()

    def create_juan(self):
        self._builder.set_name("Juan").set_age(25).set_country("Mexico").set_weight(
            80.0
        )
        return self._builder.build()


people_builder = PeopleBuilder()

hector = (
    people_builder.set_name("Hector")
    .set_age(30)
    .set_country("Colombia")
    .set_weight(70.5)
    .build()
)

print(hector)


people_director = PeopleDirector(people_builder)
juan = people_director.create_juan()
print(juan)

hector = people_director.create_hector()
print(hector)
