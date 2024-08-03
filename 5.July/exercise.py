import mysql.connector as myconnec
class calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def functionality(self):
        self.add = self.a + self.b
        self.sub = self.a - self.b
        self.mult = self.a * self.b
        self.div = self.a / self.b
        print('Addition: ', self.add)
        print('subtraction: ', self.sub)
        print('multiple: ', self.mult)
        print('Divison: ', self.div)
        
class DatabaseManager(calculator):

    def __init__(self, a, b):
        super().__init__(a, b)
        self.mydb = myconnec.connect(host = "localhost", user ="root", password ="223412", database = 'lesson')
        self.mycursor = self.mydb.cursor()

    def insert_into_db(self):
        self.functionality()  # Perform calculations first #the calculation is done
        insert = 'INSERT INTO calculator (addition, subtraction, multiple, division) VALUES (%s, %s, %s, %s)'
        values = (self.add, self.sub, self.mult, self.div)
        self.mycursor.execute(insert, values)
        self.mydb.commit()
        print("Data inserted successfully")

a = int(input('Enter A: '))
b = int(input('Enter B: '))
seng = DatabaseManager(a, b)
seng.insert_into_db()