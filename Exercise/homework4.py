#Exercise 1

class student:
    def _init_(self):
        self.name = ''
        self.reg_num = ''
    def display(self):
        print(self.name)
        print(self.reg_num)
access = student()

access.name = 'Seng'
access.reg_num = '113412'

access.display()

'''
#Exercise 2
class fruit:
    def _init_(self):          #constructor
        self.color = ''
        self.kilogram = ''
        self.price = ''
    def detail(self):
        print(self.color)
        print(self.kilogram)
        print(self.price)
apple = fruit()
orange = fruit()
jackfruit = fruit()

apple.color = 'Red'
apple.kilogram = '50g'
apple.price = '1000 Riel'

orange.color = 'orange'
orange.kilogram = '20g'
orange.price = '500 Riel'

jackfruit.color = 'yellow'
jackfruit.kilogram = '100g'
jackfruit.price = '1500 Riel'

apple.detail()
orange.detail()
jackfruit.detail()
'''