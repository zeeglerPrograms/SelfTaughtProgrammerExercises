import csv 

#find a file on your computer and print its contents
with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/st.txt", "r") as f:
    print(f.read())

#ask user a question and print that to a file
answer = input("What is your favorite color? ")
with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/favoritecolor.txt", "w") as f:
    f.write(answer)

#take data from a list of lists and write them to a CSV file
listOfLists = [["Top Gun", "Risky Business", "Minority Report"], ["titanic", "The Revenant", "Inception"], ["Training Day", "Man On Fire", "Flight"]]

with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/movies.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for list in listOfLists:
        sublistTerms = []
        for sublist in list:
            sublistTerms.append(sublist)
        w.writerow(sublistTerms)