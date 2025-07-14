from abc import ABC, abstractmethod


class TaxStrategy(ABC):
    @abstractmethod
    def calculate_tax(self, amount: float) -> float:
        pass


class IVAStrategy(TaxStrategy):
    def calculate_tax(self, amount: float) -> float:
        return amount * 0.21  # 21% IVA


class IRPFStrategy(TaxStrategy):
    def calculate_tax(self, amount: float) -> float:
        return amount * 0.15  # 15% IRPF


class TaxCalculator:
    def __init__(self, tax_strategy: TaxStrategy):
        self.__tax_strategy = tax_strategy

    def set_tax_strategy(self, tax_strategy: TaxStrategy):
        self.__tax_strategy = tax_strategy

    def calculate(self, amount: list[float]) -> list[float]:
        taxes = []
        for amt in amount:
            taxes.append(self.__tax_strategy.calculate_tax(amt))
        return taxes


# Ejemplo de uso
iva_strategy = IVAStrategy()
irpf_strategy = IRPFStrategy()

tax_calculator = TaxCalculator(iva_strategy)
print(tax_calculator.calculate([100, 200, 300]))
# Salida: [21.0, 42.0, 63.0]

tax_calculator.set_tax_strategy(irpf_strategy)
print(tax_calculator.calculate([100, 200, 300]))
# Salida: [15.0, 30.0, 45.0]

# iva_strategy = IVAStrategy()
# irpf_strategy = IRPFStrategy()

# tax_calculator = TaxCalculator(iva_strategy)
# print(tax_calculator.calculate_tax(100))  # Salida: 21.0

# tax_calculator.set_tax_strategy(irpf_strategy)
# print(tax_calculator.calculate_tax(100))  # Salida: 15.0
