
'''

Dibujar un cuadrado con bucles

'''

#Forma 1
'''
num = int(input("Dame un numero: "))

for row in range(num):
    print('')
    for col in range(num):
        print('*',end='')

print('')
'''
#Forma 2
num = int(input("Dame un numero: "))

print('*'* num)

for row in range(num):
    print('*'+' '*(num-2)+'*')

print('*'* num)



