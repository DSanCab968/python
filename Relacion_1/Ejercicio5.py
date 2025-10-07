'''

Ejercicio 5

Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde.

'''

horas = float(input("¿Cuántas horas trabajas al dia? "))
pagaHora = float(input("¿Y a cuanto cobras la hora? "))
pagaDiaria = horas * pagaHora
print(f"Te tienen que pagar {pagaDiaria} €")