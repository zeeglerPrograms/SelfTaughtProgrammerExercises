#ChapterFourExercises

#write a function that takes a number and squares it
def squared(x):
    return x * x

number = int(input('Enter a number to have it squared: '))
print(squared(number))

#write a function that accepts string as a parameter and prints it
def printString(string):
    print(string)

strToPrint = str(input('Please enter a string: '))
printString(strToPrint)

#write a function that takes two required and two optional parameters
def requiredAndOptional(par1, par2, par3, x = None, y = None ):
    if x == None or y == None:
        if x == None:
            result = y + par1 + par2 + par3
        elif y == None:
            result = y + par1 + par2 + par3
        else:
            result = par1 + par2 + par3
    else:
        result = x + y + par1 + par2 + par3
    return result

#Write two functions:
    #fun1:  Take integer and return result divided by 2
    #fun2: Take integer as value and return result multiplied by 4
# call first function, save result as a variable, and use it as var in fun2
def fun1(x):
    return x / 2

def fun2(x):
    return x * 4

x = int(input('Enter an integer: '))
y = fun1(x)
z = fun2(y)
print(f'{z} is the result of {x} divided by 2, multiplied by 4.')

#write a function that converts string to float. Use exception handling to deal with errors
def strToFloat(stringVal):
    try: 
        return float(stringVal)
    except ValueError:
        newInput = print('Error. You must enter a number.')

strVal = str(input('please enter a number: '))
print(strToFloat(strVal))

"""
This is an example of a docstring
containing many lines of text.
And heres a third line to prove it
"""