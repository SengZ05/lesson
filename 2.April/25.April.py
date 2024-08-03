'''
class Naga:
    def _init_ (self):
        self.name = ''
        self.age = ''
    def bill (self):
        print('welcome %s' %self.name)
        print('You are %d years old' %self.age)
seng = Naga()

seng.name = input('Name: ')
seng.age = int(input('Age: '))

seng.bill()
'''
'''
class calculator:
    def _init_ (self):
        self.a = ''
        self.b = ''
    def add(self):
        print(('sub: %d')%(self.a + self.b))
    def multi(self):
        print(('Mul: %d')%(self.a * self.b))
    def sub(self): #we can change to specific objective that we want to allow to use this function
        print(('Sub: %d')%(self.a - self.b))
testing = calculator()

testing.a = int(input('A: '))
testing.b = int(input('B: '))

testing.add()
testing.multi()
testing.sub()
'''

#instance variable
'''
class calculator:
    def __init__(self,num1,num2):#(sinet,5,10)
        self.a=num1 #5
        self.b=num2
    def add(self):
        print('Addiion', self.a + self.b)
    def mul(self):
        print('mul', self.a * self.b)
    def div(self):
        print('div', self.a/self.b)
    def sub(self):
        print('sub', self.a -self.b)

sinet=calculator(5,10)
sinet.add()
sinet.mul()
siha=calculator(8,12)
siha.div()
'''
'''
#Class variable
class laptop:
    name = 'Alienware' #class variable
    def _init_ (self, price, memory):
        self.price = price
        self.memory = memory #instance variable
    def output(self):
        print(self.name)
        print(self.price)
        print(self.memory)
laptop.name = 'Asus' #update name without changing code
seng = laptop(2000, 16)

seng.output()
'''

#access to class variable by using classname.variable
#access to function fucntion by using self function