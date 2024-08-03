#everything is clear use for loop
#if it isn't that clear use while loop
#exercise 1

i = 0
while (i != 10):
    i += 1
    print(i, end="")
    print('\r')

#exercise 2

i = 10
while(i>0):
    print(i)
    i-=1

# -= means subtract by 1 repeatedly
# += means add by 1 repeatedly
# /= means divide by 1 repeatedly


a = int(input("Enter factorial number: "))
x = 1
for i in range(x, a+1):
    x *= i
print(x)


n = 4
a = 1
while(n>1):
    a += 1
    a = a*n
    print(a)



