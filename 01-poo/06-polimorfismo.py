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


class Barman(People):
    """A subclass of People that represents a Barman."""

    pass

    def welcome(self):
        print(f"Welcome to the bar, my name is {self.name} and I am your barman!")


class Student(People):
    """A subclass of People that represents a Student."""

    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession

    def hi(self):
        """Override the hi method to include profession."""
        print(f"Hello, my name is {self.name} and I am a {self.profession} student.")


def show(people):
    people.hi()


hector = Student("Hector", 20, "Ingeniero")

juan = People("Juan", 30)

show(hector)
show(juan)

# Polimorphism allows us to use the same interface (method `hi`) for different types of objects.
# In this case, both `Student` and `People` have a `hi` method, so we can call it on both objects.
# This is the essence of polymorphism: different classes can be treated as instances of the same class through a common interface.
# This allows for more flexible and reusable code.