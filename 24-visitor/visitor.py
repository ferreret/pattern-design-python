# Patrón de diseño visitor

# El patrón de diseño visitor permite agregar nuevas operaciones a una jerarquía de clases
# sin modificar las clases existentes.

from abc import ABC, abstractmethod
import math

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle"):
        pass
    
    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle"):
        pass

class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class Circle(Element):
    def __init__(self, radius: float):
        self.radius = radius
    
    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)

class Rectangle(Element):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)

class AreaCalculator(Visitor):
    def visit_circle(self, circle: "Circle"):
        area = math.pi * circle.radius ** 2
        print(f"El área del círculo es: {area}")
    
    def visit_rectangle(self, rectangle: "Rectangle"):
        area = rectangle.width * rectangle.height
        print(f"El área del rectángulo es: {area}")

class PerimeterCalculator(Visitor):
    def visit_circle(self, circle: "Circle"):
        perimeter = 2 * math.pi * circle.radius
        print(f"El perímetro del círculo es: {perimeter}")
    
    def visit_rectangle(self, rectangle: "Rectangle"):
        perimeter = 2 * (rectangle.width + rectangle.height)
        print(f"El perímetro del rectángulo es: {perimeter}")

circle = Circle(10)
rectangle = Rectangle(10, 20)

area_calculator = AreaCalculator()
circle.accept(area_calculator)
rectangle.accept(area_calculator)

perimeter_calculator = PerimeterCalculator()
circle.accept(perimeter_calculator)
rectangle.accept(perimeter_calculator)

