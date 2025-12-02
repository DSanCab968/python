'''

Ejercicio 13

Escribir un programa que pregunte por una muestra de números, separados por
comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

'''
lista = []

x = input("Escribe numeros separados por comas: ")


for n in x.split(","):
    lista.append(float(n))

media = sum(lista)/len(lista)

varianza = sum((x - media) ** 2 for x in lista) / len(lista)
desviacion = varianza ** 0.5

print(f"La media es {media} y la desviacion tipica {desviacion}")
