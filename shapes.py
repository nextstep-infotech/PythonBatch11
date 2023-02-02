class Shape:
    name = "Geometric Shapes" #Class variable
    
    def print_name(self):
        print(self.name)

    def get_area(self):
        return None

class Rectangle(Shape):
    name = 'Rectangle'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)

class Triangle(Shape):
    name = 'Triangle'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return (self.width*self.height)/2

    
class Circle(Shape):
    PI = 22/7
    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.PI*self.radius**2
