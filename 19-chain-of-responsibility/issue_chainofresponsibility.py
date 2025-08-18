from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, issues, next=None):
        self._issues = issues
        self._next = next

    @abstractmethod
    def handle(self, issue):
        pass


class Level1Support(Handler):
    def handle(self, issue):
        if issue in self._issues:
            print(f"Nivel 1: Resolviendo '{issue}'.")
        elif self._next:
            print("Nivel 1: Escala el problema al siguiente nivel.")
            self._next.handle(issue)


class Level2Support(Handler):
    def handle(self, issue):
        if issue in self._issues:
            print(f"Nivel 2: Resolviendo '{issue}'.")
        elif self._next:
            print("Nivel 2: Escala el problema al siguiente nivel.")
            self._next.handle(issue)


class SupportManager(Handler):
    def handle(self, issue):
        print(f"Gerente de soporte: Resolviendo '{issue}'.")


manager = SupportManager([])
level2 = Level2Support(["bug", "user_delete", "exception"], manager)
chain = Level1Support(["password_reset", "user_create"], level2)

# chain.handle("bug")
chain.handle("database_error")
