'''
Ejercicio 5

Escribir un programa que almacene el diccionario con los créditos de las asignaturas
de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
tiene <créditos> créditos, donde <asignatura> es cada una de las
asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar
también el número total de créditos del curso.

'''
asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

x = 0
for i in asignaturas:
    print(f"La asignatura {i} tiene {asignaturas[i]} creditos")
    x += asignaturas[i]

print(f"Los creditos totales son {x}")


