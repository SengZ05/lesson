# read fucntion with python
# import os
# os.path.isfile("C:\\Users\\SengZ\\Documents\\school\\T.Dinesh\\Semester I\\peepee.txt")
#list = ['peeepee\n', 'cat is cute\n', 'I hate exam\n']
# file = open("C:\\Users\\SengZ\\Documents\\school\\T.Dinesh\\Semester I\\peepee.txt", "r")


# read file
# file.read() read all content
# file.read(n) read by character
# file.readlines() read and showing in list form
# join statement is used to create space or put something in between
# with statement, we can use file without closing it
# with open("C:\\Users\\SengZ\\Documents\\school\\T.Dinesh\\Semester I\\peepee.txt", "r") as file:
#     output = file.readlines()
# information = " ".join(output)
#output1 = file.read(20)
    # print(output)
import os
filename = input("Enter file path: ")
if os.path.isfile(filename):
    print("yes, its present")
    file = open(filename, "r")
    output = file.read()
    print(output)
else:
    print("nope")