'''
Hacer un triangulo rectangulo

'''
'''
num = int(input("Dime un numero: "))

for row in range(0,num+1):
    print('*'*row)

'''
'''
impimir la diagonal del triangulo

'''
'''
num = int(input("Dime un numero: "))

for row in range(num):
    print(' '*row + '*')
'''

'''

triangulo rectagulo al reves

'''

'''
num = int(input("Dime un numero: "))

for row in range(num,0,-1):
    print('*'*row)
'''

#la diagonal

num = int(input("Dime un numero: "))

for row in range(num,0,-1):
    print(' '*row+'*')