'''
Ejercicio 7

Escribir una función que reciba una muestra de números en una lista y devuelva otra
lista con sus cuadrados.

'''

def listaCuadrados(lista):

    cuadrados=[]
    for i in lista:
        cuadrados.append(i**2)

    return cuadrados



listaIni = [2,4,6]
listaFin = listaCuadrados(listaIni)
print(listaFin)