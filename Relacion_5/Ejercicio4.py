'''

Ejercicio 4

Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor

'''

while True:
    num = int(input("Introduzca los ganadores de la loteria: "))
              
    if num == 000:
        break
    else:
        numeros = []
        numeros.append(num)

print(numeros.sort())



