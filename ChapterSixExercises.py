#ChapterSixExercises

#print every character in the string "Camus"
strVal = "Camus"
for char in strVal:
    print(char)

#write a program that takes two strings from user, and inserts them into string
str1 = str(input('Enter a string: '))
str2 = str(input('Enter another string: '))
finalString = 'Yesterday I wrote a {}. I sent it to the {}!'.format(str1, str2)
print(finalString)

#use a method to make the first character in a string uppercase
strToCap = 'aldous Huxley was born in 1894.'
strToCap = strToCap.replace('aldous', 'Aldous')
print(strToCap)

#take the string "Where now? Who Now? When Now?" and make it return as
    #["Where Now?", "Who Now?", "When Now?"]
originalString = "Where now? Who Now? When Now?"
finalList = []
splitString = originalString.split('?')
for sentence in splitString:
    if sentence != '':
        withPunctuation = sentence + '?'
        finalList.append(withPunctuation)
print(finalList)

#take a list and turn it into a astring. There should be space between 
    #each word but no space between the word fence and the period that follows it
sentList = ["The", "fox", "jumped", "over", "the", "fence", "."]
sentList = " ".join(sentList)
sentList = sentList.replace(' .', '.')
print(sentList)

#replace every instance of 's' in string with dollar sign
string = "A screaming comes across the sky."
string = string.replace('s', '$')
print(string)

#use a method to find the first instance of 'm' in 'Hemmingway'
name = 'Hemmingway'
index = name.index('m')
print(index)

#put quotes into a string
string = "\"Hello\", she said."
print(string)

#create the string "three three three" using concatenation, and then again using multiplication
string = 'three '
conc = string + string + string
mult = string * 3
print(f'Concoctination is: {conc}. Multiplication is: {mult}')

#slice a string to only include characters before the comma
string = "It was a bright cold day in April, and the clocks were striking thirteen."
index = string.index(',')
print(string[:index])