def calculator():
    try:
        a = int(input('A: '))
        b = int(input("B: "))
        print(a/b)
    except:
        print('Error')
    else:
        print('works baby')
    finally:
        print('How was it?')
calculator()