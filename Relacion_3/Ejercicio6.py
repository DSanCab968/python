'''
Ejercicio 6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.


'''

nombreUser = input("Dime tu nombre: ")
sexoUser = input("Eres hombre o mujer? Escribe h para hombre o m para mujer: ")

if sexoUser.upper() == "H":
    if nombreUser[0] >= "N":
        print("Eres del grupo A")
    else: print("Eres del grupo B")
elif sexoUser.upper() == "M":
    if nombreUser[0] <= "M":
        print("Eres del grupo A")
    else: print("Eres del grupo B")

    
