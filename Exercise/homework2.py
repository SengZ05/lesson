#exercise 1

'''
for i in range(1, 5+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
'''
#exercise 2
'''
for i in range(1, 6):
    print('')
    print('week : ', i)
    print('----------------')
    for j in range(1, 3):
        print('\t\tDay : ', j)
'''
#exercise 3
'''
for i in range(0, 5): #loop from 0 to 5
    for j in range(0, i+1): #if the i is o, then the j would be 1 since j = i+1
        print("*   ",end="") #end= is used to print item horizontal
    print() #this used to prevent the start align in the same line
'''

a = int(input('Enter row:'))
for i in range(a):
    for j in range(i+1):
        print('* ', end="")
    print()

