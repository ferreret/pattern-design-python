class People:

    class_variable = "I am a class variable"

    def __init__(self, name: str):
        self.name = name

    def hi(self):
        print(f"Hello, my name is {self.name}")

    @staticmethod
    def static_method():
        print(
            "This is a static method, it does not depend on instance or class variables."
        )

    @classmethod
    def class_method(cls):
        print(
            f"This is a class method, it can access class variables: {cls.class_variable}"
        )


hector = People("Hector")
hector.hi()

hector.static_method()
People.static_method()

hector.class_method()
People.class_method()
