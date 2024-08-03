#For Loop
'''
for i in(1, 2, 3, 4):
    print(i)
'''
'''
#for loop with range
for i in range(1, 10):
    print(i)
'''
'''
for i in range(1, 11):
    print('%d ^ 2 = %d' %(i, i**2))
'''
a = int(input('a: '))
b = int(input('b: '))
for i in range(a, b):
    print('\r%d'%(i+1))
