'''

Ejercicio 4

Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor

'''

numeros = []

while True:
    num = int(input("Introduce numeros ganadores(0 para terminar): "))
    if num == 0:
        break
    else:
        numeros.append(num)

print(f"Números ganadores ordenados: {sorted(numeros)}")




