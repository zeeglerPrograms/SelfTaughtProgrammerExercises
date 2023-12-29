#ShapesClasses

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))

#making a child class
class Square(Shape):
    def area(self):
        return self.width * self.len
    # you can overwrite a parent method by redefining it for the child
        # this is called "method overriding"
    def print_size(self):
        print("""I am {} by {}""".format(self.width, self.len))

my_shape = Square(20, 25)
print(my_shape.area())
my_shape.print_size()