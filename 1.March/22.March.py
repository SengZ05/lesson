
a = input('Enter Usename : ')
b = input('Enter Password : ')
if(a=='Seaturtle' and b=='111'):
    print('Hello Turtle')
else:
    print('incorrect username or password')


a = int(input('Enter the value for a :'))
b = int(input('Enter the value for b :'))
c = a%b
print(c)
if (a%b==0):
    print('true')
else:
    print('False')

a = input('Do you want to have a six-pack ? ( yes/no ) :')
if(a=='yes'):
    b=input('Do you want to go to the gym ? ( yes/no ) :')
else:
    print('congrat , you recive your big cute belly !! ')
if(b=='yes'):
    print('Let\'s go , you gonna get a six-pack !! ')
else:
    print('congrat , you recieve your big cute belly !! ')


a = input('Do you have a business idea ? ( yes/no ) :')
if(a=='yes'):
    print('Start your own business')
else:
    print('You will be a worker')


a = int(input('Enter your score :'))
if(a>=50):
    print('Congrat , you pass ')
else:
    print('you fail')

a = input('Enter your grade (A/B/C/D/E/F) : ')
if(a=='A'):
    print('You got the KIT scholarship')
else:
    print('You need to pay')



a = int(input('Enter value for a : '))
b = 4
c = 5
d = a%b
e = a%c
if((d and c)== 0):
    print(f'{a}%{b}={d} and {a}%{c}={e}')
else:
    print('the number is not divisble by 4 and 5')
