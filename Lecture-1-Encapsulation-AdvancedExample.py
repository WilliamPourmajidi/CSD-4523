# # # Encapsulation Advance Example
# #
class BankAccountAdvance:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_details(amount, "Deposit")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            self.__transaction_details(amount, "Withdrawal")

    def __transaction_details(self, amount, type):
        print(f"{type} of ${amount} was successful. Current balance: ${self.__balance}")


# Usage
account = BankAccountAdvance("Elon")
account.deposit(1000)
account.withdraw(300)
# #


##########################################

# # # Encapsulation Advance Example
# #
# # class BankAccountAdvance:
# #     def __init__(self, owner, balance=0):
# #         self.owner = owner
# #         self.__balance = balance
# #
# #     def deposit(self, amount):
# #         if amount > 0:
# #             self.__balance += amount
# #             self.__transaction_details(amount, "Deposit")
# #         else:
# #             print("Deposit amount must be positive")
# #
# #     def withdraw(self, amount):
# #         if amount > self.__balance:
# #             print("Insufficient balance")
# #         else:
# #             self.__balance -= amount
# #             self.__transaction_details(amount, "Withdrawal")
# #
# #     def __transaction_details(self, amount, type):
# #         print(f"{type} of {amount} was successful. Current balance: {self.__balance}")
# #
# # # Usage
# # account = BankAccountAdvance("Bob Johnson")
# # account.deposit(300)
# # account.withdraw(150)
# #
#
# ## Inheritance Simple Examples
# # class Vehicle:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model
# #
# # class Car(Vehicle):
# #     pass
# #
# # # Usage
# # my_car = Car("Toyota", "Corolla")
# # print(my_car.brand, my_car.model)
# #
#
# ## Inheritance Intermediate Examples
# # class Vehicle:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model
# #
# #     def start(self):
# #         print("Engine started")
# #
# # class Car(Vehicle):
# #     def __init__(self, brand, model, horsepower):
# #         super().__init__(brand, model)
# #         self.horsepower = horsepower
# #
# #     def start(self):
# #         super().start()
# #         print(f"{self.model} with {self.horsepower} horsepower engine started")
# #
# # # Usage
# # my_car = Car("Honda", "Civic", 180)
# # my_car.start()
#
# ## Inheritance Advance Examples
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def start(self):
#         print("Engine started")
#
# class Car(Vehicle):
#     def __init__(self, brand, model, horsepower):
#         super().__init__(brand, model)
#         self.horsepower = horsepower
#
#     def start(self):
#         super().start()
#         print(f"{self.model} with {self.horsepower} horsepower engine started")
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model, horsepower=0)
#         self.battery_capacity = battery_capacity
#
#     def start(self):
#         print(f"{self.model} with {self.battery_capacity} kWh battery started - silent and powerful!")
#
# # Usage
# my_ecar = ElectricCar("Tesla", "Model S", 100)
# my_ecar.start()
#


# def deposit(self, amount):
#     if amount > 0:
#         self.__balance += amount
#         print(f"Added {amount} to the balance")
#     else:
#         print("Deposit amount must be positive")
#
#
# # # Usage
# # account = BankAccount("John Doe")
# # account.deposit(100)
# #


#
# ## Inheritance Simple Examples
# # class Vehicle:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model
# #
# # class Car(Vehicle):
# #     pass
# #
# # # Usage
# # my_car = Car("Toyota", "Corolla")
# # print(my_car.brand, my_car.model)
# #
#
# ## Inheritance Intermediate Examples
# # class Vehicle:
# #     def __init__(self, brand, model):
# #         self.brand = brand
# #         self.model = model
# #
# #     def start(self):
# #         print("Engine started")
# #
# # class Car(Vehicle):
# #     def __init__(self, brand, model, horsepower):
# #         super().__init__(brand, model)
# #         self.horsepower = horsepower
# #
# #     def start(self):
# #         super().start()
# #         print(f"{self.model} with {self.horsepower} horsepower engine started")
# #
# # # Usage
# # my_car = Car("Honda", "Civic", 180)
# # my_car.start()
#
# ## Inheritance Advance Examples
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def start(self):
#         print("Engine started")
#
# class Car(Vehicle):
#     def __init__(self, brand, model, horsepower):
#         super().__init__(brand, model)
#         self.horsepower = horsepower
#
#     def start(self):
#         super().start()
#         print(f"{self.model} with {self.horsepower} horsepower engine started")
#
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model, horsepower=0)
#         self.battery_capacity = battery_capacity
#
#     def start(self):
#         print(f"{self.model} with {self.battery_capacity} kWh battery started - silent and powerful!")
#
# # Usage
# my_ecar = ElectricCar("Tesla", "Model S", 100)
# my_ecar.start()
#
