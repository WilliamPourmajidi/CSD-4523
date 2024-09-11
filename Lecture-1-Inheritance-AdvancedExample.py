## Inheritance Intermediate Examples
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Engine started")

class Car(Vehicle):
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model)
        self.horsepower = horsepower

    def start(self):
        super().start()
        print(f"{self.brand}, {self.model} with {self.horsepower} horsepower engine started")

# Usage
my_car = Car("Honda", "Civic", 180)
my_car.start()
