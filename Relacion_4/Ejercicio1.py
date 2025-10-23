'''

Ejercicio 1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
veces.

'''

a = 1

while a <= 10:
    palabra = input("Dime una palabra: ")
    print(f"{palabra} (nº{a})")
    a += 1