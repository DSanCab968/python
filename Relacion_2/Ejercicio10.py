'''
Ejercicio 10

Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta.

'''

compra = input("Dime lo que vas a comprar separado por comas: ")

listaCompra = compra.split(",")

for producto in listaCompra: 
    print(f"{producto} \n")
