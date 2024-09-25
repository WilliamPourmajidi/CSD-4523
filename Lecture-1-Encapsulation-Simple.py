# Encapsulation Basic Example
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print(self.__balance)


account = BankAccount("William")
account.show_balance()
print("----------------------------")
account.deposit(100)
account.show_balance()
print("----------------------------")
account.withdraw(40)
account.show_balance()

