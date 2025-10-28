'''

Ejercicio 11

Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.

'''

palabra = input("Introduce una palabra: ")

for letra in palabra[::-1]:#basicamente indicamos toda la cadena y que la recorra con paso inverso (dcha a izda)
    print(letra)



