import statistics
import math

#call a different function from the statistis module
statistics.mean([1, 2])

#create a module named cubed that returns a number cubed. import the function from another module
def cubed(number):
    return math.pow(number, 3)
print(cubed(3))