class People:

    class_variable = "I am a class variable"

    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def hi(self):
        print(f"Hello, my name is {self.name}")

    def __some_private_method(self):
        """A private method that cannot be accessed outside this class."""
        print("This is a private method.")

    @property
    def age(self):
        """Getter for the private __age variable."""
        return self.__age

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


hector = People("Hector", 20)
hector.hi()

print(hector.name)
print(hector.age)  # Accessing the private variable through the getter
print(hector.__age)  # This will raise an AttributeError because __age is private

# hector.__some_private_method()  # This will raise an AttributeError because the method is private
