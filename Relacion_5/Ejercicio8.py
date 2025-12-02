'''

Ejercicio 8

Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo

'''

palabra = input("Dime una palabra: ")
inversa = []

for letra in palabra:
    inversa.insert(0, letra)

inversa = "".join(inversa)

if palabra == inversa:
    print(f"La palabra {palabra} es un palindromo")
else:
    print(f"La palabra {palabra} no es un palindromo")


'''
Otra forma:



palabra = input("Dime una palabra: ")

if palabra == palabra[::-1]:
    print(f"La palabra {palabra} es un palindromo")
else:
    print(f"La palabra {palabra} no es un palindromo")

'''




    