#Pythong collection
#List, Tuple, Set and Dictionary

#list
a = []
print(type(a))

#tuple
b = ()
print(type(b))

#set = one value
c = {4}
print(type(c))

#dictionary =  value as a couple
#Name : x, y, x
#Age : 31, 32, 33
#Score : 56, 67, 89
d = {'Name':'Seng'}
print(type(d))
========================================================
##List
a = [45, 45, 'KIT', 4.5]
b = [411, 432, 'Kirirom', 'Seng']
print(a)

#change list

a.append(900)
a.insert(0, 'Lmao')
a.remove(45)  # the process starts from left to right and one by one
a.remove(45) #use value
a.pop() #index

a.extend(b)
print(a)
========================================================
#Tuple statis value
a = (2, 'KIT', True) #we cannot add or modified it
#casting change data type
b = list(a)
b.append(90)
print(b)
b.insert(1, 'Seng')
print(b)
========================================================
#set = the index could be updated base on some situation
a = {'seng', 89, 54, 'lmao'}
print(a) #it's random, can't mention by index and duplicate, can add and remove value
a.add(6)
a.remove(6)
print(a)
b = list(a)
print(type(b))
========================================================
#dictionary
a = {'Name':'Seng', 'Age':67} #all string
print(a)
========================================================

a = {}
b = {}
c = {}
for i in range(1, 6):
    i = (input('Name: '))
    i.add(a)
    j = (input('Age: '))
    j.add(b)
    k = (input('Score: '))
    k.add(c)
for j in range(1, 6):
    print(f'Name:{a}, Age:{b}, Score{c}')
