'''
Ejercicio 8

Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.

'''

'''
precio = input("Dime el precio exacto de algo: ")
precioEuros = precio.split(".")[0]
precioCentimos = precio.split(".")[1]
print(f"Son {precioEuros} euros y {precioCentimos} centimos.")

'''
#mas simple

precio = input("Dime el precio exacto de algo: ")
print(f"Son {precio.split(".")[0]} euros y {precio.split(".")[1]} centimos.")