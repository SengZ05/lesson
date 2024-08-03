# # Create an empty dictionary to store student information
# students = {}

# # Number of students to be entered
# num_students = int(input("Enter the number of students: "))

# # Collect student information
# for _ in range(num_students):
#     name = input("Enter the student's name: ")
#     age = int(input("Enter the student's age: "))
#     score = float(input("Enter the student's score: "))
    
#     # Store the information in the dictionary
#     students[name] = {'age': age, 'score': score}

# # Print all the collected student information
# print("\nStudent Information:")
# for name, details in students.items():
#     print(f"Name: {name}, Age: {details['age']}, Score: {details['score']}")

# import mysql.connector as myconnec
# mydb = myconnec.connect(
#     host = "localhost", 
#     user ="root", 
#     password ="223412", 
#     database = 'lesson')
# if mydb.is_connected():
#     print('connection established')
# mycursor= mydb.cursor() 


# for i in range (0, 5):
#     print('This is day: ', i)
#     for j in range (0, 5):
#         print('\tThis is what happens inside day: ', j)

# for i in range (0, 1):
#     for j in range (1, 101):
#         if j % 2 == 1:
#             print(j)

# i = 1 
# while i <= 100:
#     i += 1
#     if i % 2 == 1:
#         print(i)
        
# Create an empty dictionary to store user information
# user_data = {}

# # Number of users to input data for
# num_users = int(input("Enter the number of users: "))

# # Loop to get user input
# for i in range(num_users):
#     print(f"Enter details for user {i + 1}:")
#     name = input("Name: ")
#     age = int(input("Age: "))
#     score = float(input("Score: "))
    
#     # Insert the data into the dictionary
#     user_data[name] = {"Age": age, "Score": score}

# # Print the user data
# print("\nUser Data:")
# for name, details in user_data.items():
#     print(f"Name: {name}, \tAge: {details['Age']}, \tScore: {details['Score']}")

# data = {}

# for i in range(2):
#     name = input('Name: ')
#     age = input('Age: ')
#     score = input('Score: ')

#     data[name] = {'Age':age, 'Score':score}

# for name, details in data.items():
#     print(f'Name: {name} Age: {details['Age']} Score: {details['Score']}')

# class testing:
#     name = 'Seng'
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#     def show (self):
#         print(f'Name: {self.name}\nAge:{self.age}\nScore;{self.score}')
#     @classmethod
#     def changename(cls):
#         cls.name = input('change to:')
#         print(cls.name)
# seng = testing('seng', 12, 90)
# seng.changename()
# seng.show()

# class father:
#     def __init__(self, a, b, cal1, cal2):
#         self.cal1 = cal1
#         self.cal2 = cal2
#         self.a = a
#         self.b = b
#     def process(self):
#         self.cal1 = (self.a + self.b)
#         self.cal2 = (self.b + self.b)
#         print(self.cal1)
#         print(self.cal2)
# class son(father):
#     def __init__(self, a, b, cal1, cal2):
#         super().__init__(a, b, cal1, cal2)
# seng = son(10, 14, None, None)
# seng.process()


# change section of the student

# class login:
#     ID = []
#     def __init__(self, user_name, passowrd, ID):
#         self.user_name = user_name
#         self.password = passowrd
#     def process (self):
#         for i in range(5):
#             print('---------------------------')
#         print('Hello there!')
#         print('Here is your personal details: ')
#         print(f'Name: {self.user_name}\nID: {self.ID}\nPassword: {self.password}')
#     @classmethod
#     def change(cls):
#         change = input('Are you wish to change your ID?: (y/n) : ')
#         if change == 'y':
#             cls.ID = input('Change to : ')
#         else:
#             print('Thanks for using our service')
# name = input('Enter your name: ')
# password = input('Enter your password: ')
# ID = input('Enter your ID: ')
# seng = login(name, password, ID)
# login.change()
# seng.process()

# from abc import ABC, abstractclassmethod
# class teacher(ABC):
#     @abstractclassmethod
#     def SE(self):
#         pass
#     @abstractclassmethod
#     def TM(self):
#         pass
# class student(teacher):
#     def SE(self):
#         print('teacher is here')
#     def TM(self):
#         print('peepee')
# seng = student()
# seng.SE()

import mysql.connector as myconnection
mydb = myconnection.connect(host = 'localhost', user = 'root', password = '223412', database = 'testing')
code = mydb.cursor()

# code.execute('insert into student (id, name, subject, major) values (%s, %s, %s, %s)', ('1', 'seng', 'Python', 'SE'))
# mydb.commit()
# multi  = ('insert into student (id, name, subject, major) values (%s, %s, %s, %s)')
# peepee = [('2', 'fong', 'DSA', 'TM'), ('3', 'reach', 'DBMS', 'SE'), ('4', 'rauth', 'DBMS', 'TM')]
# code.executemany(multi, peepee)
# print('success')
# mydb.commit()
# code.execute("select * from student")
# rows = code.fetchall()
# print("fetch all records:", rows)

i = 0
a = 1
while 9 >= i:
    i -= 1
    print(i)