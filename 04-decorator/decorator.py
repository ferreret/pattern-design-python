# El patrón de diseño Decorator te permite añadir nuevas funcionalidades o comportamientos a un objeto individual de forma dinámica, sin alterar el código de otros objetos del mismo tipo.

# En tu código, tienes un BasicTaco. Los "decoradores" como DoubleMeatDecorator y ExtraCheeseDecorator actúan como envoltorios que le añaden "extras". Cada decorador envuelve al taco y añade su propio coste al precio del taco que contiene.

# De esta manera, puedes construir un taco con combinaciones flexibles (doble carne, luego queso extra) apilando decoradores uno sobre otro. El precio final se calcula sumando el coste base del taco más el de todos los ingredientes extra que lo envuelven.

# En el caso de la description, cada decorador añade su propia descripción al taco base, permitiendo que el resultado final sea una descripción completa de todos los extras añadidos.

from abc import ABC, abstractmethod


class Taco(ABC):
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class BasicTaco(Taco):
    def price(self):
        return 5.0

    def description(self):
        return "Basic Taco"


class TacoDecorator(Taco):
    def __init__(self, taco: Taco):
        self._taco = taco

    def price(self):
        return self._taco.price()

    def description(self):
        # Comportamiento por defecto para la descripción
        return self._taco.description() + " extra"


class DoubleMeatDecorator(TacoDecorator):
    def price(self):
        return self._taco.price() + 4.0

    def description(self):
        return super().description() + " Double Meat"


class ExtraCheeseDecorator(TacoDecorator):
    def price(self):
        return self._taco.price() + 1.5

    def description(self):
        return super().description() + " Cheese"


taco = BasicTaco()
print(f"Basic Taco Price: ${taco.price()}")
print(f"Basic Taco Description: {taco.description()}")

taco_with_double_meat = DoubleMeatDecorator(taco)
print(f"Taco with Double Meat Price: ${taco_with_double_meat.price()}")
print(f"Taco with Double Meat Description: {taco_with_double_meat.description()}")

cheese_taco = ExtraCheeseDecorator(taco_with_double_meat)
print(f"Taco with Double Meat and Extra Cheese Price: ${cheese_taco.price()}")
print(
    f"Taco with Double Meat and Extra Cheese Description: {cheese_taco.description()}"
)
