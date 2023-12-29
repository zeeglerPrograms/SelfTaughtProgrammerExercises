#chapter 3 exercises

#print 3 different strings
s1 = 'This is a string.'
s2 = 'This is also.'
s3 = 'This one too.'

print(f'3 Different strings are: {s1} {s2} {s3}')

#if statements
inputInteger = int(input('Please enter an integer: '))
if inputInteger < 10:
    print('This number is less than 10')
elif inputInteger >= 10 and inputInteger <= 25:
    print('This number is greater than or equal to 10, and less than or equal to 25')
elif inputInteger > 25:
    print('This number is greater than 25')

#take two variables, divide by each other, print remainder
def remainder(var1, var2):
    remainder = var1 % var2
    return remainder

#take two variables, divide, return quotient
def quotient(var1, var2):
    if var2 == 0:
        quotient = 0
    else:
        quotient = var1 / var2
    return quotient

num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))

print(f'The quotient of those two numbers is: {quotient(num1, num2)}')
print(f'The remainder of those two numbers is: {remainder(num1, num2)}')

#write a program that takes variable age and prints differents strings depending on age

def ageString(age):
    if age < 10:
        phrase = 'Single digits, buddy!'
    elif age == 10:
        phrase = 'You made it to double digits!'
    elif age > 10 and age < 20:
        phrase = 'The Tens and the Teens'
    elif age >= 20 and age  < 30:
        phrase = 'The roaring Twenties'
    elif age >= 30 and age < 40:
        phrase = 'Enjoy those Thirties'
    elif age >= 40 and age < 50:
        phrase = 'The Forties are a comin'
    elif age >= 50 and age < 60:
        phrase = 'Dance in your Fifties'
    elif age >= 60 and age < 70:
        phrase = 'The Sixties sure are fun'
    elif age >= 70 and age < 80:
        phrase = 'Here come the Seventies'
    elif age >= 80 and age < 90:
        phrase = 'Octaganerian time!!!'
    elif age >= 90 and age < 100:
        phrase = 'Nineties are more than just grunge!'
    elif age >= 100:
        phrase = 'Triple digits? Too many to count!'
    return phrase

ageInput = int(input('Please enter your age: '))

print(ageString(ageInput))