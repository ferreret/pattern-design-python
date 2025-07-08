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


hector_b = Barman("Hector", 20)
hector_b.hi()
hector_b.welcome()


hector = Student("Hector", 20, "Ingeniero")
hector.hi()


print(hector.profession)
