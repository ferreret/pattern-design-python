# Patrón de diseño Singleton
# Es de tipo creacional y garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella.


class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True
