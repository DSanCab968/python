'''
Ejercicio 7

Escribir un programa que cree un diccionario simulando una cesta de la compra. El
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
compra y el coste total, con el siguiente formato

Lista de la compra

Artículo 1  Precio
Artículo 2  Precio
Artículo 3  Precio
…
Total   Coste


'''

cesta = {}

while True:
    articulo = input("Introduce el nombre del artículo (o 'fin' para terminar): ")
    if articulo.lower() == 'fin':
        break

    while True:
        try:
            precio = float(input(f"Introduce el precio de {articulo}: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el precio.")

    cesta[articulo] = precio

print("\nLista de la compra")
total = 0

for articulo, precio in cesta.items():
    print(f"{articulo}\t{precio:.2f} €")
    total += precio

print(f"Total\t{total:.2f} €")
