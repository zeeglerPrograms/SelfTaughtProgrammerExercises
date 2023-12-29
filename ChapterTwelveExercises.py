import math
#define a class called Apple with 4 instance variables that represent four attributes of an apple
class Apple():
    def __init__(self, color, weight, name, juicyness):
        self.color = color
        self.weight = weight
        self.name = name
        self.juicyness = juicyness

app1 = Apple('red', 10, 'Pink Lady', 'Dry')
print(app1.juicyness)

#create a Circle class with a method called area that calculates and returns its area
class Circle():
    def __init__(self, r):
        self.radius = r
    
    def calculate_area(self):
        return self.radius ** 2 * math.pi
cir1 = Circle(3)
print(cir1.calculate_area())

#creat a Triangle class with a method called area that returns its area
class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
    
    def area(self):
        return (self.base * self.height) / 2
    
tri1 = Triangle(3, 5)
print(tri1.area())

#hexagon returns area
class Hexagon():
    def __init__(self, s):
        self.side = s

    def area(self):
        return ((3 * math.sqrt(3)) / 2) * (self.side * self.side)
    
hex1 = Hexagon(5)
print(hex1.area())