'''
Ejercicio 5

Escribir un programa que pida al usuario que introduzca una frase en la consola y
muestre por pantalla la frase invertida.

'''
'''
frase = input("Dime una frase aleatoria: ")
fraseInv = ''.join(reversed(frase))
print(fraseInv)

'''
#otra forma

frase = input("Dime una frase aleatoria: ")
fraseInv = frase[::-1]
print(fraseInv)