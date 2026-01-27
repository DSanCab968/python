'''
Ejercicio 11

Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
diccionario generado con la función anterior y devuelva una tupla con la palabra más
repetida y su frecuencia

'''

def contar_palabras(cadena):
    
    palabras = cadena.lower().split()
    frecuencias = {}

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


def palabra_mas_repetida(diccionario):
  
    palabra_max = None
    frecuencia_max = 0

    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia

    return palabra_max, frecuencia_max


texto = "hola mundo hola python hola mundo"
dic = contar_palabras(texto)
resultado = palabra_mas_repetida(dic)

print(dic)
print(resultado)
