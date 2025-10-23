'''

Ejercicio 3

Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas.

'''

num = abs(int(input("Dime un numero entero: ")))

impares = []

for i in range(1, num + 1):
    if i % 2 != 0:
        impares.append(str(i))
        
print(", ".join(impares))

