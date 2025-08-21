# Patrón de diseño de tipo comportamiento
# Mediator

# El mediador es un objeto que centraliza la comunicación entre objetos
# y reduce las dependencias entre ellos.

# Ejemplo:
# En una aplicación de chat, el mediador es el servidor, y los clientes
# son los usuarios. El servidor actúa como mediador, y los usuarios
# se comunican entre sí a través del servidor.

# Ventajas:
# - Reduce las dependencias entre objetos, lo que facilita la mantenibilidad
#   y la escalabilidad de la aplicación.
# - Centraliza la comunicación, lo que facilita el seguimiento de las
#   interacciones entre objetos.
# - Facilita la adición de nuevos objetos a la aplicación, ya que no es
#   necesario modificar los objetos existentes.

# Desventajas:
# - El mediador puede convertirse en un punto único de fallo, lo que
#   puede afectar la disponibilidad de la aplicación.
# - Puede ser difícil de diseñar y implementar un mediador que sea
#   eficiente y escalable.

from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, event: str):
        pass

class BaseComponent:
    def __init__(self):
        self._mediator = None
    
    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

class ComponentA(BaseComponent):
    def hi(self):
        print("Hi, I'm A")  
        self._mediator.notify("A")
    
    def response(self):
        print("A is responding")

class ComponentB(BaseComponent):
    def hi(self):
        print("Hi, I'm B")  
        self._mediator.notify("B")
    
    def response(self):
        print("B is responding")

class ConcreteMediator(Mediator):
    def __init__(self, component_a: ComponentA, component_b: ComponentB):
        self._component_a = component_a
        self._component_b = component_b
        self._component_a.set_mediator(self)
        self._component_b.set_mediator(self)
    
    def notify(self, event: str):
        if event == "A":
            self._component_b.response()
        elif event == "B":
            self._component_a.response()
        else:
            print("Unknown event")

if __name__ == "__main__":
    a = ComponentA()
    b = ComponentB()
    mediator = ConcreteMediator(a, b)
    a.hi()
    b.hi()
    



