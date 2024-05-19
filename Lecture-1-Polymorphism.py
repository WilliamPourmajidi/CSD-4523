class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle, we are going to draw circle by identifying a point (x,y) and a radius for our circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

def draw_shape(shape):
    shape.draw()


# Usage
shapes = [Circle(), Square()]
print(f"Length of our shape list: {len(shapes)}")
print(type(shapes))
for shape in shapes:
    draw_shape(shape)
