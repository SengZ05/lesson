#abstract : create a layout for future edit like an empty bucket of function
#subtract : use to add or override function to abstract
from abc import ABC, abstractmethod
class student(ABC):
    @abstractmethod
    def SE(self):
        pass
    @abstractmethod
    def TM(self):
        pass
class SE(student):
    def score(self):
        print('the score is 50')
class display1(student):
    def SE(self):
        print('Batch 12', 36)
    def TM(self):
        print('Batch 4', 10)
    def AR(self):
        print('Batch 2', 15)
obj = display1()
obj.score()  
obj.AR()
# if we create 2 abstracts method, we have to pass 2 argument to that
from abc import ABC, abstractmethod
class student(ABC):
    @abstractmethod
    def SE(self):
        pass
    @abstractmethod
    def TM(self):
        pass
class SE2(student):
    def SE(self):
        print('SE passed')
    def TM(self):
        pass
class TM(SE2):
    def SE1(self):
        pass
    def TM1(self):
        print('TM passed')
obj = TM()
obj.SE()
obj.TM1()