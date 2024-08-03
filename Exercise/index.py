user = input('Enter your code: ')
if ('s' not in user):
    print('invalid code')
else:
    index = user.replace('s', '')
    wrap = int(index)
    index1 = wrap/10
    if(index1 % 2 == 1):
        final = index1 - 1
        print('your index is : %d ' %(final))
    else:
        print('your index is : %d ' %(index1))
