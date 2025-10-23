'''

Ejercicio 6

Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****

'''

num = abs(int(input("Dime un numero: ")))


for i in range (1, num +1):
    print("*" * i)



