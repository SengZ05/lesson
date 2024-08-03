def login():
    username = 'dinesh'
    password = 123
    a = str(input('Username: '))
    b = int(input('Password: '))
    if( a == username and b == password):
        print('Log in successfully')
    elif( a != username and b != password ):
        print('Wrong Username and Password')
    elif ( a != username):
        print('Wrong Username')
    elif( b != password):
        print('Incorrect Password')
login()