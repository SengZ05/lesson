#exercise 1
'''
a = int(input('A: '))
b = int(input('B: '))
for i in range(a, b+1):
    print(i)
'''
#exercise 3
'''
a = int(input('A: '))
b = int(input('B: '))
for i in range(a, b+1):
    if(i%2 == 0):
        print(i)
'''
#exercise 2
'''
for i in range(1, 10):
    if(i%2==0):
        print(i)
'''
#exercise 4
'''
print('even numbers:')
for i in range(1, 100):
    if(i%2==0):
        print(i)
print('Odd numbers: ')
for j in range(1, 100):
    if(j%2==1):
        print(j)
'''
#exercise 5
'''
for i in range(1, 100):
    if(i%3==0 and i%5==0):
        print(i)
'''
#exercise 6
'''''
a = int(input('a: '))
b = int(input('b: '))
total_sum = 0
for i in range(a, b+1):
    total_sum = total_sum + i
print(total_sum)
'''
#exercise 6
'''
count = 0
for i in range(1, 100):
    if(i%3==0 and i%5==0):
        count = count + 1
print(count)
'''