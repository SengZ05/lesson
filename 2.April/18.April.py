'''
#addition
def add():
    a=int(input('Enter a:'))
    b=int(input('Enter b:'))
    c=a+b
    print(c)

add()

def add():
    a=int(input('Enter a:'))
    b=int(input('Enter b:'))
    c=a+b
    return c

result=add() # 5+5=10
print(result)

def add():
    a=int(input('Enter a:'))
    b=int(input('Enter b:'))
    c=a+b
    return a,b,c
result=add() # 5+5=10
print(result)
a,b,c=add()
print(a)

#parametera, arguments

def add(a,b):
    c=a+b
    print(c)
    
add(10,5)
'''
def get_numbers():
    numbers = [float(input("Enter a number: ")) for i in range(5)]
    print("List of numbers:", numbers)
    

# Example usage:
get_numbers()


