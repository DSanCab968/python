'''

Ejercicio 4

Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.

'''

num = abs(int(input("Dime un numero entero: ")))

cuenta = []
x = 0

while x <= num:
    cuenta.append(str(num))
    num -= 1
        
print(", ".join(cuenta))