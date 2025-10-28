'''

Ejercicio 12

Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.

'''

frase = input("Dime un frase: ")
letra = input("Dime una letra: ")

numLetras = frase.count(letra)

print(numLetras)



