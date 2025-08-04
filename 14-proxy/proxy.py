# El patrón del tipo proxy es de tipo estructural
# Se utiliza un objeto intermediario para crear otro objeto
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def action(self):
        pass


class RealSubject(Subject):
    def action(self):
        print("RealSubject: Handling action.")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self.__real_subject = real_subject
        self.__authorized = False

    def action(self):
        if self.__authorized:
            self.__real_subject.action()
        else:
            print("Proxy: Unauthorized action.")

    def login(self, username: str, password: str):
        if username == "user" and password == "pass":
            self.__authorized = True


def some(subject: Subject):
    subject.action()


real_subject = RealSubject()
# some(real_subject)

proxy = Proxy(real_subject)
some(proxy)

proxy.login("user", "pass")
some(proxy)


