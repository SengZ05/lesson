'''
class bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit1(self):
        a = int(input('Deposit value: '))
        print('Deposit: %d\nRemain Total: %d' %(a, self.balance - a))
    def withdraw1(self):
        b = int(input('withdraw value: '))
        print('withdraw: %d\nRemain Total: %d' %(b, self.balance - b))
class saving_account(bank_account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.account_number = account_number
        self.balance = balance
    def deposit2(self):
        a = int(input('Deposit value (from saving account): '))
        print('Deposit: %d\nRemain Total: %d' %(a, self.balance - a))
    def withdraw2(self):
        b = int(input('withdraw value (from saving account): '))
        print('withdraw: %d\nRemain Total: %d' %(b, self.balance - b))
class checking_account(saving_account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.account_number = account_number
        self.balance = balance
    def deposit3(self):
        a = int(input('Deposit value(from checking account): '))
        print('Deposit: %d\nRemain Total: %d' %(a, self.balance - a))
    def withdraw3(self):
        b = int(input('withdraw value (from saving account): '))
        print('withdraw: %d\nRemain Total: %d' %(b, self.balance - b))
a = int(input('Enter your ID: '))
if a == 1122:
    b = 1000
elif a == 1133:
    b = 100
else:
    print('invalid ID')
c = int(input('what account do you want to use? ( 1 == checking account , 2 == saving account ): '))
if c == 1:
    obj = checking_account(a, b)
    obj.deposit3()
    obj.withdraw3()
elif  c == 2:
    obj = saving_account(a, b)
    obj.deposit2()
    obj.withdraw2()
'''
'''
class employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
    def display_detailsDev(self):
        print("employee's name: %s\nID: %d" %(self.name, self.id))
    def display_detailsMA(self):
        print("employee's name: %s\nID: %d\nSalary: %d" %(self.name, self.id, self.salary))
class developer(employee):
    def __init__ (self, name, id, salary = None):
        super().__init__(name, id, salary)
        self.name = name
        self.id = id
        self.salary
class manager(employee):
    def __init__ (self, name, id, salary):
        super().__init__(name, id, salary)
        self.name = name
        self.id = id
        self.salary
obj = manager('seng', 1122, 1000)
obj.display_detailsMA()
'''
'''
class person:
    def __init__(self, name):
        self.name = name
class student(person):
    def __init__(self, grade, name = []):
        super().__init__(name)
        self.grade = grade
    def display(self):
        print('Name: '+self.name)
        print('grade: '+self.grade)
obj = student('A', 'seng')
obj.display()
'''
class vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
class car(vehicle):
    def __init__(self, model, manufacturer = []):
        super().__init__(manufacturer)
        self.model = model
    def display_info(self):
        print('manufacturer: '+self.manufacturer)
        print('model: '+self.model)
obj = car('AAA', 'BBB')
obj.display_info()