a = int(input('Enter your salary: '))
b = int(input('Enter your age: '))
if(a>3000 or b>35):
    c = int(input('Enter your loan: '))
    if(c>30000):
        print('The amount of loan is exceeded')
    else:
        print('You are done')
else:
    print('you are not eligible for the laon')

