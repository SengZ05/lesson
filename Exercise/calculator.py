a = int(input("Enter A: "))
c = (input("Enter the operator ( + , - , * , / ): "))
b = int(input("Enter B: "))

if(c=='-'):
    print('%d %s %d = %d' %(a, c, b, a-b))
elif(c=='+'):
    print('%d %s %d = %d' %(a, c, b, a+b))
elif(c=='*'):
    print('%d %s %d = %d' %(a, c, b, a*b))
elif(c=='/'):
    print('%d %s %d = %d' %(a, c, b, a/b))
else:
    print('invalid input')