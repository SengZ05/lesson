# Method/function
# 1 instance method (self) (create object) (access def using object) 
# 2 class method (cls) (no need object) (access def using class)
# 3 static method (no key word) (object) (access def using nothing)
# 2 and 3 come up with decorator

class student:
    section = 'A'
    def _init_ (self, name):
        self.name = name
    def detail (self):
        print(self.name)
student.section = 'B' # change out side class and function
student.name = 'seng'
print(student.name)

#print(student.section) #print the whole structure to see

# class method # no self
class student:
    section = 'A'
    def _init_ (self, name):
        self.name = name
    def detail (self):
        print('Name: ', self.name)
        print(self.section)
    @classmethod 
    def changeclassvariable(cls):
        cls.section = input('change to:')
        print(cls.section)

seng = student()
seng.changeclassvariable()   #show changes using object

student.changeclassvariable()  
#show changes using class (mention class name) but if using @classmethod (no need to mention class name )

#static method
# no cls and self
class student:
    section = 'A'
    def __init__(self, name):
        self.name=name
    def detail (self):
        print('Name: ', self.name)
        print(self.section)
    @classmethod 
    def changeclassvariable(cls):
        cls.section = input('change to:')
        print(cls.section)
    @staticmethod
    def studentwellbeing():
        print('I\'m good')
parinha = student('seng')
parinha.detail()