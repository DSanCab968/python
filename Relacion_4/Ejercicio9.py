'''

Ejercicio 9

Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.

'''
cont = "contraseña"

while True:
    contIntro = input("Dime la contraseña: ")
    if contIntro == cont:
        print("¡Contraseña correcta! Acceso permitido.")
        break
    else:
        print("Contraseña incorrecta. Intentalo de nuevo.")