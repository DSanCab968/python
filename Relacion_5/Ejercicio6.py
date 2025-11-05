'''

Ejercicio 6

Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir

'''

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatura in asignaturas:
    nota = float(input(f"Dime la nota que sacaste en {asignatura}: "))
    notas.append(nota)

suspensas = []
for i in range(len(asignaturas)):
    if notas[i] < 5:
        suspensas.append(asignaturas[i])

if suspensas:
    print("Tienes que repetir las siguientes asignaturas:")
    for materia in suspensas:
        print(materia)
else:
    print("Has aprobado todo")


