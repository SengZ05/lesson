#super keyword
#parent class -  constructor
#child class - constructor

class father:
    def __init__(self, age, name):
        self.name = name
        self.age = age
        print('Parent class constructor(name) :'+self.name)
    def display(self):
        print('PArent class method')

class son(father):
    def __init__(self, age, name):
        super().__init__(age, name)
        self.age = age
        print('Child class constructor (age):', self.age)
    def display(self):
        super().display()
        print('Child class method')
obj=son('21', 'seng')
obj.display()

#poly

def add(a, b, c=0):
    d = a + b + c
    print(d)
add(12, 34, 11)
'''
'''
#method overriding for class (method, same function name , son is prioritize so in order to access to father class, use super key)
class father:
    def face(self):
        print('sharp nose, powerful jawline')
class son(father):
    def face(self):
        print('great jawline')
class daughter(father):
    def face(self):
        super().face()
        print('sharp nose')
obj = daughter()
obj.face()

#method overriding for def (parameter, change parameter in the function rather than in the class)
class student:
    def name_of_student(self, name = None):
        print('Name: ', name)
student1 = student()
student1.name_of_student('seng')

#Encapsulation
#private and public
#private
class KIT:
    __president_name = 'DR.kamaga'  #public variable
    def __display(self, qualification): #public function
        print('Name: ' ,self.__president_name)
        print('Qualificaiton', qualification)
    def info(self, qualification):
        self.__display(qualification)
#between 2 classes - super
#within class - self
obj = KIT()
obj.info('phD')

#public
class KIT:
    president_name = 'DR.kamaga'  #public variable
    def display(self, qualification): #public function
        print('Name: ' ,self.president_name)
        print('Qualificaiton', qualification)
obj = KIT()
obj.display('phD')
'''