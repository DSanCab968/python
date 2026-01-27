'''
Ejercicio 8

Escribir una función que reciba una muestra de números en una lista y devuelva un
diccionario con su media, varianza y desviación típica.

'''

import math

def estadisticas(lista):
    if len(lista) == 0:
        return {'media': None, 'varianza': None, 'desviacion_tipica': None}
    
    n = len(lista)
    
    # Media
    media = sum(lista) / n
    
    # Varianza (desviación al cuadrado)
    varianza = sum((x - media) ** 2 for x in lista) / n  # Varianza poblacional
    
    # Desviación típica
    desviacion_tipica = math.sqrt(varianza)
    
    return {
        'media': media,
        'varianza': varianza,
        'desviacion_tipica': desviacion_tipica
    }

# Ejemplo de uso
muestra = [4, 8, 6, 5, 3, 7]
resultado = estadisticas(muestra)
print(resultado)
