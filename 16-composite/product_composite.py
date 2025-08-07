from abc import ABC, abstractmethod


class SaleComponent(ABC):
    @abstractmethod
    def get_total(self) -> float:
        pass

    @abstractmethod
    def details(self, space=0):
        pass


class Product(SaleComponent):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_total(self):
        return self.__price

    def details(self, space=0):
        print(" " * space + f"- Producto {self.__name}, Precio: {self.__price}")


class Package(SaleComponent):
    def __init__(self, name):
        self.__name = name
        self.__products = []

    def add_product(self, product: SaleComponent):
        self.__products.append(product)

    def remove_product(self, product: SaleComponent):
        self.__products.remove(product)

    def get_total(self):
        total = 0
        for product in self.__products:
            total += product.get_total()
        return total

    def details(self, space=0):
        print(" " * space + f"- Paquete {self.__name}, Total: {self.get_total()}")
        for product in self.__products:
            product.details(space + 2)


product1 = Product("Camisa", 20)
product2 = Product("Pantalón", 30)
product3 = Product("Zapatos", 50)

package1 = Package("Ropa de Verano")
package1.add_product(product1)
package1.add_product(product2)

package2 = Package("Outfit Completo")
package2.add_product(package1)
package2.add_product(product3)

package2.details()
print(f"Total de la compra: {package2.get_total()}")
