'''

Ejercicio 5

Escribir un programa que almacene en una lista los números del 1 al 10 y los
muestre por pantalla en orden inverso separados por comas

'''

numeros = []
i=1

while i <= 10:
    numeros.append(i)
    i+=1

print(numeros)

numerosRev = []
for a in numeros[::-1]:
    numerosRev.append(a)

print(numerosRev)
    



