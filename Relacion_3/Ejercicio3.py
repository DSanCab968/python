'''
Ejercicio 3

Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.


'''

num1 = float(input("Dime un numero: "))
num2 = float(input("Dime otro numero: "))

if num2 != 0:
    print(num1/num2)
else:
    print("Error")