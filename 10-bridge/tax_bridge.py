from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        pass


class LocalTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> float:
        return amount * 0.05


class ForeignTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount: float) -> float:
        return amount * 0.10


class AbastractSale(ABC):
    def __init__(self, tax_calculator: TaxCalculator, concepts):
        self.tax_calculator = tax_calculator
        self.concepts = concepts

    @abstractmethod
    def calculate_total(self) -> float:
        pass


class Sale(AbastractSale):
    def calculate_total(self) -> float:
        total = sum(self.concepts)
        tax = self.tax_calculator.calculate_tax(total)
        return total + tax


# Example usage
sale = Sale(LocalTaxCalculator(), [100, 200, 300])
print(
    f"Total with local tax: {sale.calculate_total()}"
)  # Output: Total with local tax: 630.0

foreign_sale = Sale(ForeignTaxCalculator(), [100, 200, 300])
print(
    f"Total with foreign tax: {foreign_sale.calculate_total()}"
)  # Output: Total with foreign tax: 660.0
