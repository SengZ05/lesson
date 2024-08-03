a = 'KIT'
b = '2019'
print(f'I joined {a} in {b} ')

name = 'Reach'
age = 19
salary = 2000.56
print('name : %s , age : %d ,salaray : %.2f' %( name , age , salary))

collage_name = 'KIT'
My_father_name = 'Meach'
MY_mother_name = 'Samros'
print('I studied at {x} , My father name is {y} and My mother name is {z}.' .format(x=collage_name,y=My_father_name,z=MY_mother_name))

values = (1,2,3,4,'Reach', True)
print(values[4])

values = ('Reach','Jakriya',18 , 19)
print('My name is {x} , I\'m {y} year old and This is my friend , His name is {z} and he\'s {a} year old.' .format(x=values[0],y=values[3],z=values[1],a=values[2]))

a = input('Username :')
b = input('Password :')
print(type(a))

a = input()
print(float(a))

print('*\n**\n***\n****\n*****\n******')
print('\n')
print('******\n*****\n****\n***\n**\n*')
print('\n')
print('******\n*    *\n*   *\n*  *\n* *\n*')

# 1. Frist exercise
a = input('Your name :')
b = input('Your age :')
c = input('Your Address :')
d = input('Your Country :')
print('My Name is :' , a)
print('My age is :', b)
print('Address : \n\t' , c)
print('\t' , d)

# 2. Second exercise
a = int(input('Enter the value of a : '))
b = int(input('Enter the value of b : '))
c = int(input('Enter the value of c : '))
d = a*b*c
e = a+b+c
f = d/e
print('Multiply all 3 values = ', d )
print('Add all the 3 values = ',e )
print('Divide the multiplied value by the added value = ', f )  

# 3. Third exercise
a = input('Your name : ')
b = input('Your Department : ')
c = int(input('Your Score : '))
d = 10
e = c/d
print('Name : ',a, '\nDepartmet : ',b, '\nScore : ',c, '\nMy Score is : ',e,'/10')
