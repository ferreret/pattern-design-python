class People:

    class_variable = "I am a class variable"

    def __init__(self, name: str):
        self.name = name

    def hi(self):
        print(f"Hello, my name is {self.name}")


hector = People("Hector")
hector.hi()

print(hector.class_variable)
print(People.class_variable)
