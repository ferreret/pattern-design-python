# Patrón de diseño template method
# Este patrón define el esqueleto de un algoritmo en una operación,
# delegando algunos pasos a las subclases.
# Esto permite a las subclases redefinir ciertos pasos de un algoritmo
# sin cambiar su estructura.

from abc import ABC, abstractmethod

class BeerBrewing(ABC):
    def ferment(self):
        print("Fermentar la cerveza durante 2 semanas")

    @abstractmethod
    def select_ingredients(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass

    def bottle(self):
        print("Embotellar")

    def prepare(self):
        self.select_ingredients()
        self.ferment()
        self.add_extras()
        self.bottle()
        
class LagerBeer(BeerBrewing):
    def select_ingredients(self):
        print("Malta clara, lúpulo suave y levadura lager")
    
    def add_extras(self):
        print("Gas extra")

class StoutBeer(BeerBrewing):
    def select_ingredients(self):
        print("Malta tostada, lúpulo intenso y levadura Ale")

    def add_extras(self):
        print("Notas de café y chocolate")

class SourBeer(BeerBrewing):
    def select_ingredients(self):
        print("Malta suave, lúpulo suave y levadura Ale")

    def add_extras(self):
        print("Notas de cítrico y cítrico")

    def ferment(self):
        print("Fermentar la cerveza durante 4 semanas")

lager = LagerBeer()
lager.prepare()
print("----")
stout = StoutBeer()
stout.prepare()
print("----")
sour = SourBeer()
sour.prepare()
