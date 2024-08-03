#Break and continue statement 

'''
for i in range(1, 5):
    if(i>0):
        print(i)
        break #if used continue the loop will keep going until the end
                #if used break the loop will break at the first print event the loop is 1 to 5
print('KIT')
'''
#break is used to escape from loop
#continue is used to continue to loop 
#break
'''
for i in range(1, 9):
    print('This is %d.' %(i))
    if(i==6):
        break
print('Exiting for loop')
print('Not in loop')
'''
print('loop starts')
for i in range(1, 100):
    print('This is %d' %(i))
    if(i<=8):
        continue   
    else:
        break
print('Not in loop') 
