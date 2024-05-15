class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

def make_sound(animal):
    animal.sound()

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    make_sound(animal)
