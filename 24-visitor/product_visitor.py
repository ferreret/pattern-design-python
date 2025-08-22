from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def accept(self, visitor: "CalculatorVisitor"):

        pass

class Book(Product):
    def __init__(self, price: float):
        self.price = price

    def accept(self, visitor: "CalculatorVisitor"):
        visitor.visit_book(self)

class Food(Product):
    def __init__(self, price: float):
        self.price = price

    def accept(self, visitor: "CalculatorVisitor"):
        visitor.visit_food(self)

class CalculatorVisitor(ABC):
    @abstractmethod
    def visit_book(self, book: "Book"):
        pass

    @abstractmethod
    def visit_food(self, food: "Food"):
        pass

class TaxCalculatorVisitor(CalculatorVisitor):
    def visit_book(self, book: "Book"):
        tax = book.price * 0.1
        print(f"El impuesto del libro es: {tax}")

    def visit_food(self, food: "Food"):
        tax = food.price * 0.2
        print(f"El impuesto de la comida es: {tax}")

class DiscountCalculatorVisitor(CalculatorVisitor):
    def visit_book(self, book: "Book"):
        discount = book.price * 0.15
        print(f"El descuento del libro es: {discount}")

    def visit_food(self, food: "Food"):
        discount = food.price * 0.25
        print(f"El descuento de la comida es: {discount}")

book = Book(100)
food = Food(200)

tax_calculator = TaxCalculatorVisitor()
book.accept(tax_calculator)
food.accept(tax_calculator)

discount_calculator = DiscountCalculatorVisitor()
book.accept(discount_calculator)
food.accept(discount_calculator)