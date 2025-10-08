'''
Ejercicio 11

Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

'''

producto = input("Dime un producto: ")
precio = float(input("Dime el precio: "))
unidades = int(input("Dime cuantos quieres: "))
total = unidades*precio


print(f"{producto}: {precio:08.2f} x {unidades:03d} = {total:010.2f}")