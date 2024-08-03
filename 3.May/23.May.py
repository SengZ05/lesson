
a = int(input('Enter armstrong number: '))
b = len(str(a))
sum = 0
loop = a
while loop > 0:
    digit = loop % 10
    sum += digit ** b
    loop //= 10
if a == sum:
    print('True')
else:
    print('False')


e_list = []
num = str(input("Enter number to check if it's a armstrong numbers or not: "))
for i in num: 
    a = int(i) ** len(num)
    e_list.append(a)
arm = sum(e_list)
if int(num) == arm:
    print(num, "is an armstrong number")
else:
    print(num,"isn't an armstrong number")


def cube_sum_first_n():
    list = []
    for i in range(4):
        a = int(input('Enter number: '))
        list.append(a)
    sqaure = [x **3 for x in list]
    print(sqaure)
    return sqaure
cube_sum_first_n()
