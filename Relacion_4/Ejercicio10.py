'''

Ejercicio 10

Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.

'''

num = int(input("Introduce un número entero: "))

if num <= 1:
    print(f"{num} no es primo.")
else:
    es_primo = True
    for i in range(2, int(num**0.5) + 1):#lo de la raiz cuadrada
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{num} es primo.")
    else:
        print(f"{num} no es primo.")
