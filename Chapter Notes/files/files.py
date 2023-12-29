st = open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/st.txt", "w")
st.write("Hi from Python!")
st.close()

#a better way to do this is an automatically closing with statement
# with open([file_path],[mode]) as [variable_name]: [your_code]
with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/st.txt", "w") as f:
    f.write("Hello dude")

with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/st.txt", "r") as f:
    print(f.read())

#you can only call read on a file once without reopening it so 
    #its best to save contents to a variable or container

my_list = list()

with open("/Users/daniel/PythonProjects/SelfTaughtProgrammer/files/st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)