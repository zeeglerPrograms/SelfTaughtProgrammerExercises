#csvFiles

import csv

with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))