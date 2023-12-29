#classes

#classes always start with a capital letter, in camelCase
    #methods are small functions that only affect the object the class creates
    #method names, like function names should be:
        #all underscore with '_' between words
            # like_this

#method is like a function but it must be
    # 1. defined as a suite of a class
    # 2. it has to accept at least one parameter
        # so it is standard to create 'self' as a parameter
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")
    
    def rot(self, days, temp):
        self.mold = days * temp


#creating a new object in the class is called:
    # instantiating a class
or1 = Orange(10, 'dark orange')

#you can change value of object by [object].[variable] = [new_value]
or1.weight = 100
or1.color = 'light orange'

or2 = Orange(9, 'dark orange')
or3 = Orange(14, "yellow")

# gives memory address
print(or1)
# to access values do this:
print(or1.weight)
print(or1.color)

# adding a model/method rot
newOrange = Orange(6, "neworange")
newOrange.rot(10, 98)
print(newOrange.mold)


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width * self.len
    
    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())