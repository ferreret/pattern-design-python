from abc import ABC, abstractmethod

class Account:
    def __init__(self, balance: float):
        self.__balance = balance
    
    def deposit(self, amount: float):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}")
    
    def withdaw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdaw {amount}. New balance is {self.__balance}")
        else:
            print("Not enough balance")

class Command(ABC):
    def __init__(self, account: Account) -> None:
        self._account = account
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class DepositCommand(Command):
    def __init__(self, account: Account, amount: float) -> None:
        super().__init__(account)
        self._amount = amount
    def execute(self):
        self._account.deposit(self._amount)
    def undo(self):
        self._account.withdaw(self._amount)

class WithdawCommand(Command):
    def __init__(self, account: Account, amount: float) -> None:
        super().__init__(account)
        self._amount = amount
    def execute(self):
        self._account.withdaw(self._amount)
    def undo(self):
        self._account.deposit(self._amount)


class TransactionManager:
    def __init__(self) -> None:
        self._commands = []
    
    def execute_command(self, command: Command):
        command.execute()
        self._commands.append(command)
    
    def undo_last_command(self):
        if self._commands:
            command = self._commands.pop()
            command.undo()
            print("Undo last command, new balance is", account._Account__balance)


        else:
            print("No commands to undo")


account = Account(100)
transaction_manager = TransactionManager()

deposit_command_200 = DepositCommand(account, 200)
withdraw_command_100 = WithdawCommand(account, 100)

transaction_manager.execute_command(deposit_command_200)
transaction_manager.execute_command(deposit_command_200)
transaction_manager.execute_command(withdraw_command_100)

transaction_manager.undo_last_command()



