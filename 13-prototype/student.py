from abc import ABC, abstractmethod
from typing import Self
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Self:
        pass


class Student(Prototype):
    def __init__(
        self,
        name,
        age,
        gender,
        school_id,
        grade,
        school_email,
        school_phone,
        school_address,
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.school_id = school_id
        self.grade = grade
        self.school_email = school_email
        self.school_phone = school_phone
        self.school_address = school_address

    def clone(self) -> Self:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return (
            f"Nombre: {self.name}, Edad: {self.age}, Género: {self.gender},"
            f" ID de la Escuela: {self.school_id}, Nota: {self.grade}, Email de la Escuela: {self.school_email},"
            f" Teléfono de la Escuela: {self.school_phone}, Dirección de la Escuela: {self.school_address}"
        )


student = Student(
    "Prototype Student",
    20,
    "Hombre",
    "123456789",
    "5",
    "contact@school.com",
    "513548687",
    "Independecia 1535",
)

juan = student.clone()
juan.name = "Juan"

pedro = student.clone()
pedro.name = "Pedro"

print(student)
print(juan)
print(pedro)
