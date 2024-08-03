a = []
for i in range(1, 5):
    num = int(input('a: '))
    a.append(num)
    num = num + i
print(a)
print('The sum is %d' %(num))