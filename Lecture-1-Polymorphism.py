class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

def draw_shape(shape):
    shape.draw()

# Usage
shapes = [Circle(), Square()]
for shape in shapes:
    draw_shape(shape)
