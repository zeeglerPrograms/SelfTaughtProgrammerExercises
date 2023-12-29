#ChapterSevenExercises

#print each item in list
list = ["The Walking Dead", "Entourage", "the Sopranos", "the Vampire Diaries"]
for show in list:
    print(show)

#print all numbers 25 to 50
for i in range(25, 51):
    print(i)

#write a program with an infinite loop 'type q to quit' and a list of numbers
list = [25, 30, 89, 53]
while True:
    userInput = input('Guess a Number to see if its on the list. Enter \'q\' to quit: ')
    if userInput == 'q':
        break
    if int(userInput) in list:
        print("That number was in the list!")
    else:
        print("Guess Again!")

#multiply all numbers in list a with all numbers in list b and append each result to a third list
listA = [8, 19, 148, 4]
listB = [9, 1, 33, 83]
listC = []
for x in listA:
    for y in listB:
        listC.append(x * y)
print(listC)