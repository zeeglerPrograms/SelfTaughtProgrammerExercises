#ChapterThirteenExercises

#create rectangle and square classes with a method called calculate_perimeter
    # that calculates the perimeter of the shapes
# create rectangle and square objects and call this method on both of them

#create a class called Shape. Redefine the square and rectangle to inherit shape
    # define a method called what_am_i that prints "i am a shape" when called
class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4
    
    # define a method that lets user change side size by a number
    def change_size(self, num):
        self.side += num

class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.len + self.width)
    
sq1 = Square(8)
re1 = Rectangle(2, 4)

sq1.what_am_i()
re1.what_am_i()

sizeChange = int(input('How much would you like to change the square by? Enter an integer: '))
sq1.change_size(sizeChange)
print(sq1.calculate_perimeter())
print(re1.calculate_perimeter())

#use Composition to model a horse that has a rider

class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

rid1 = Rider("Mr. Ridersworth")
h1 = Horse("Mrs. Horsington", rid1)
print(f'{h1.name} is ridden by: {h1.rider.name}.')