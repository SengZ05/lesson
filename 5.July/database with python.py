import mysql.connector as myconnec
mydb = myconnec.connect(host = "localhost", user ="root", password ="223412", database = 'test')
mycursor= mydb.cursor() 

#test #KIT

#create database
# mycursor.execute("create database test")

#create table
# mycursor.execute("create table info (name varchar(25), age int, contact int)")

#insert
#mycursor.execute("insert into info (name, age, contact) values (%s, %s, %s)", ('devin', '25', '0974242017'))

#update
# mycursor.execute("update info set name = %s where contact = %s", ('Fong', '0974242016'))

#delete
# mycursor.execute('delete from info where contact = %s', ('0974242016',))

#insert by user input
# a = input('Name: ')
# b = input('Age: ')
# c = input('contact: ')
# mycursor.execute('insert into info (name, age, contact) values (%s, %s, %s)', (a, b, c))

#calculation
# a = int(input('A: '))
# b = int(input('B: '))
# mycursor.execute("insert into calculator (addition, subtraction, multiple, division) values (%s, %s, %s, %s)", (a+b, a-b, a*b, a/b))

# a = ('insert into info (name, age, contact) values (%s, %s, %s)')
# b = [('liza', '18', '1122'), ('rauth', '18', '2233'), ('reach', '19', '3344')]
# mycursor.executemany(a,b)
# mydb.commit()
# print(mycursor.rowcount, 'Updated')
# print('Yes')

