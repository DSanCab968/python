'''
Ejercicio 8

Escribir un programa que cree un diccionario de traducción español-inglés. El
usuario introducirá las palabras en español e inglés separadas por dos puntos, y
cada par <palabra>:<traducción> separados por comas. El programa debe
crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
no está en el diccionario debe dejarla sin traducir.

'''

entrada = input("Introduce las palabras y sus traducciones (formato palabra:traducción, palabra:traducción,...): ")

diccionario = {}
pares = entrada.split(",") 
for par in pares:
    if ':' in par:
        esp, eng = par.split(":", 1) 
        diccionario[esp.strip()] = eng.strip() 


frase_es = input("Introduce una frase en español: ")

palabras = frase_es.split()  
frase_traducida = []

for palabra in palabras:

    frase_traducida.append(diccionario.get(palabra, palabra))

print("Frase traducida:", " ".join(frase_traducida))
