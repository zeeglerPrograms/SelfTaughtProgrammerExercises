#ChapterFourteenExercises

#add a square_list class variable to a class called Square so that
    # every time you create a new square object, the new object gets added to the list

class Square():
    # make a variable called square list that adds every square made into it
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self.side)

    def __repr__(self):
        return """{} by {} by {} by {}""".format(self.side, self.side, self.side, self.side)
    
    def same_square(self, other):
        if self is other:
            return True
        else:
            return False
        
s1 = Square(3)
s2 = Square(5)

print(Square.square_list)
print(s1)
print(s1.same_square(s1))
