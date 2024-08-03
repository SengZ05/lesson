#inheritance

#single

class father:
    def phone(self):
        print('We can play games')

class son(father):
    def laptop(self):
        print('laptop for education')

bunsou=son() #object of son class
bunsou.laptop()
bunsou.phone()
'''

# multiple inheritance
'''
class father:
    def phone(self):
        print('We can play games')
        
class mother:
    def ipad(self):
        print("The ipad is good")
        
class son(father,mother):
    def laptop(self):
        print('laptop for education')

seng=son() #object of son class
seng.ipad()
seng.phone()
seng.laptop()

#multi inheritance

class father:
    def phone(self):
        self.a = str(input('Enter who you are: '))
        if(self.a == 'son'):
            print('We can play games')
        if(self.a == 'mom'):
            print('phone checked')
        else:
            print('theifffffff')
class mother(father):
    def message(self):
        print('Message received')
    def ipad(self):
        print("The ipad is good")
        
class son(mother):
    def laptop(self):
        print('laptop for education')
seng=son() #object of son class

#hierarchical 
class father:
    def phone(self):
        self.a = str(input('Enter who you are: '))
        if(self.a == 'son'):
            print('We can play games')
        if(self.a == 'mom'):
            print('phone checked')
        else:
            print('theifffffff')
class mother(father):
    def message(self):
        print('Message received')
    def ipad(self):
        print("The ipad is good")
        
class son(father):
    def laptop(self):
        print('laptop for education')
class daughter(father):
    def makeup(self):
        print('cuteee')
seng=son() #object of son class
