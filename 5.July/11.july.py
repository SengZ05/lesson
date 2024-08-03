# File handling
# there are two type of files : txt file amd binary file
# +++++++ open
'''
file = open("C:\\Users\\SengZ\\Documents\\school\\T.Dinesh\\Semester I\\peepee.txt") #txt file data
file = open(r"C:\\Users\\SengZ\\Documents\\school\\T.Dinesh\\Semester I\\peepee.txt") #raw file no thinking about \n or \t
print('file open successful')
'''
# +++++++ mode open and read
# read ==> cursor blinking on the top of the document (file is not avialable error would be file not found)
# write ==> write mode would create a new file there is no file with that name, it would overwritten by the new file
# use append mode will not overwrite the file but it edit like extra content into it
# r+ ==> we can read and write
# w+ ==> write and read
# a+ (append)==> add and read   
# for binary = rb, wb, r+b (add b to every command)
# without using mode command the default mode is read mode
'''
# step 1
file = open("C:\\Users\\SengZ\\Documents\\school\\T.Dinesh\\Semester I\\peepee.txt", "r")
# step 2
print("Name of the file: ", file.name)
# step 3
print("mode of the file", file.mode)
# mode property
print("file mode: ", file.readable())
print('file mode: ', file.writable())

file.close()

print("file is closed or not?", file.closed)
'''
file = open("C:\\Users\\SengZ\\Documents\\school\\T.Dinesh\\Semester I\\test3.txt", "w")
file.write('hello there')
# use list with writelines in order to add multiple sentences
file.close()