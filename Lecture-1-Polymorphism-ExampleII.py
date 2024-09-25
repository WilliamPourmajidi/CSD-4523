class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement 'sound' abstract method")

class Dog(Animal):
    def sound(self):
        print("Woof!")
    def food(self):
        print("As a dog I can eat everything that humans eat!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

def make_sound(animal):
    animal.sound()

# # Usage
# instantiation of objects
my_dog = Dog()
my_cat = Cat()

# putting objects in a list
animals = [my_dog, my_cat]

#passing elements of objects to make_sound function
for animal in animals:
    make_sound(animal)
