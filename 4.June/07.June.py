
class calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        print(self.a + self.b)
    def subtract(self):
        print(self.a - self.b)
    def multi(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)
seng = calculator(10, 5)
seng.addition()
seng.subtract()
seng.multi()
seng.division()

#class variablee
#instance variable
#class method and instance method
class laptop:
    brand = 'alienware'
    def __init__(self, Ram, SSD, VGA):
        self.Ram = Ram
        self.SSD = SSD
        self.VGA = VGA
    def output(self):
    #everything with self. is instance method
        print('Ram: ', self.Ram)
        print('SSD: ', self.Ram)
        print('VGA: ', self.VGA)
        print('brand: ', self.brand)
    @classmethod 
    #class method when we use cls to change sth
    def changebrand(cls):
        cls.brand = 'Asus'
        print('Updated brand: ', cls.brand)
    @staticmethod
    def display():
        print('display is kood')

laptop.changebrand()
seng = laptop(64, 2, 1050)
seng.output()
seng.display()

#instance : use self. everywhere and use it as variable within class and function
#class method : use cls in parameter and mention it as cls.
#statismethod : use it within class with using self or cls, just freedom



class father:
    def __init__(self, name):
        self.name = name
    def name(self):
        print(self.name)
class son(father):
    def __init__(self, age):
        self.age = age
        super().__init__()
    def display(self):
        print(self.age)

