# Inheritance Simple Examples
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

#defining the subclass with no business logic
class Car(Vehicle):
    pass

# Usage
my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)

