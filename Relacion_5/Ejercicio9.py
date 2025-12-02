'''

Ejercicio 9

Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal

'''
palabra = input("Dime una palabra: ")

a = palabra.count("a")
e = palabra.count("e")
i = palabra.count("i")
o = palabra.count("o")
u = palabra.count("u")

print(f"A: {a} | E: {e} | I: {i} | O: {o} | U: {u}")