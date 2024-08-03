def create_account():
    name = str(input('Enter your name: '))
    length1 = len(name)
    if(length1>15):
        print('only 15 characters')
    password = int(input('Enter your password: '))
    length2 = len(password)
    if(length2<8):
        print('at least 8 character')
    print('Account has been create successfully')

    
print('\t\tWelcome to our Bank')
print('\tAre you a new user or old user? \nPress (1) for new user\nPress (2) for old user')
log  = int(input('Answer: '))
if(log == 1):
    create_account()
