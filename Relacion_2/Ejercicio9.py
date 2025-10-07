'''
Ejercicio 9

Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
anterior para que también funcione cuando el día o el mes se introduzcan con un
solo carácter.

'''

fechaNacimiento = input("Dime la fecha en que naciste en el formato dd/mm/aa: ")

dia = fechaNacimiento.split("/",2)[0]
mes = fechaNacimiento.split("/",2)[1]
año = fechaNacimiento.split("/",2)[2]

if len(dia)<2: dia = "0" + dia
if len(mes)<2: mes = "0" + mes

print(f"El dia es {dia}, el mes {mes} y el año {año}.")
