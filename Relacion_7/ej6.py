'''
Ejercicio 6

Escribir una función que reciba una muestra de números en una lista y devuelva su
media.

'''

def listaMedia(*valores):
    total = 0
    for i in valores:
        total += i
    media = total / len(valores)
    return media

resultado = listaMedia(1, 4, 5, 6, 9)
print(resultado)
