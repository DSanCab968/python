'''
Ejercicio 1

Escribir un programa que pregunte el nombre del usuario en la consola y un número
entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
como el número introducido

'''

nombreUsuario = input("Cual es tu nombre: ")
numInt = int(input("Cuantas veces quieres ver tu nombre: "))
print(f"{nombreUsuario}\n"*numInt)