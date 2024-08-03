#iteration (step)

for i in range (1, 10): #use for loop when we know the number of iteration
    print(i) #9 iteration

#array the same data type
#list different data type

a = [1, 2, 3, 4]
a.append(6)
print(a)
a.remove(3)
print(a)
a.insert(0, 5) #use index
print(a)

#remove or append sth we use only value

a = []
for i in range(1, 5):
    num = int(input('a: '))
    a.append(num)
    num = num + i
print(a)
print('The sum is %d' %(num))
'''
#nested loop
'''
for i in range(1, 6):
    print('')
    print('week : ', i)
    print('----------------')
    for j in range(1, 3):
        print('\t\tDay : ', j)

for i in range(1, 6):
    for j in range(i-1):
        print(j)

n = int(input().strip())
    if (n%2=1):
        print('Weird')
    elif (n%2=0 and n<=5):
        print('Not Weird')
    elif (n%2=0 and n>=6 and n<=20):
        print('Weird')
    elif (n%2=0 and n>20):
        print('Not Weird')       

