# class (Naga) is a combination of varibale and function (room, game, food)
# in order to use the class, we need variable
# object (human) can be created within each class
# no object, no class
class naga:
    def _init_(self): #constructor
        self.pay = ''      #create variable in function
        self.idcard = ''
    def food(self):
        print(self.pay)
        print('enjoy food')
    def game(self):
        print(self.idcard)
        print('enjoy game')
    def room(self):
        print('enjoy sleeping')
sanji = naga()       #access to class
chopper = naga()     #access to class

sanji.pay = '100'
sanji.idcard = 'passport'    #use variable to gain access to class
chopper.pay = '150'
chopper.idcard = 'medID' 

sanji.game() #mention function what to use
sanji.food()
chopper.room()
