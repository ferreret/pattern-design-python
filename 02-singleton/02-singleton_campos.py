# Patrón de diseño Singleton
# Es de tipo creacional y garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella.


class Singleton:
    _instance = None

    def __new__(cls, name=None, age=None):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.name = name
            cls._instance.age = age

        return cls._instance


singleton1 = Singleton("Héctor", 30)
singleton2 = Singleton("Juan", 25)
singleton3 = Singleton()

print(singleton1 is singleton2)  # True

print(singleton1.name)  # Héctor
print(singleton1.age)  # 30

print(singleton2.name)  # Héctor
print(singleton2.age)  # 30

print(singleton3.name)  # Héctor
print(singleton3.age)  # 30
