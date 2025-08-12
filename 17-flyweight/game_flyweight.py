from abc import ABC, abstractmethod


class TypeCar(ABC):
    @abstractmethod
    def print(self, x, y):
        pass


class TypeCarCommon(TypeCar):
    def __init__(self, name, color, model) -> None:
        self.name = name
        self.color = color
        self.model = model

    def print(self, x, y):
        print(f"Car {self.name} color {self.color} model {self.model} at ({x}, {y})")


class CarFactory:
    def __init__(self) -> None:
        self.cars = {}

    def get_car(self, name, color, model) -> TypeCar:
        key = (name, color, model)
        if not key in self.cars:
            print(f"Creando carro {key}")
            self.cars[key] = TypeCarCommon(name, color, model)
        return self.cars[key]


class Car:
    def __init__(self, x, y, type_car: TypeCar) -> None:
        self.x = x
        self.y = y
        self.type_car = type_car

    def print(self):
        self.type_car.print(self.x, self.y)


class Game:
    def __init__(self) -> None:
        self.cars = []
        self.car_factory = CarFactory()


    def add_car(self, x, y, name, color, model):
        type_car = self.car_factory.get_car(name, color, model)
        self.cars.append(Car(x, y, type_car))

    def print_cars(self):
        for car in self.cars:
            car.print()


game = Game()

game.add_car(100, 15, "Ferrari", "Rojo", "2020")
game.add_car(200, 15, "Ferrari", "Rojo", "2020")
game.add_car(300, 15, "Ferrari", "Rojo", "2020")
game.add_car(400, 15, "Porsche", "Rojo", "2020")

game.print_cars()