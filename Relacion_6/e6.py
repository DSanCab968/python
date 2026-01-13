'''
Ejercicio 6

Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
debe imprimirse el contenido del diccionario.

'''

persona={}

nombre = input("Dime tu nombre: ")
persona["nombre"]=nombre
print(persona)

edad = input("Dime tu edad: ")
persona["edad"]=edad
print(persona)

sexo = input("Dime tu sexo: ")
persona["sexo"]=sexo
print(persona)

direccion = input("Dime tu direccion: ")
persona["direccion"]=direccion
print(persona)

telefono = input("Dime tu telefono: ")
persona["telefono"]=telefono
print(persona)

correo = input("Dime tu correo: ")
persona["correo"]=correo
print(persona)

