'''
Ejercicio 3

Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''

def factorial(numero):
    calculo=1
    cont = 1

    while cont<numero:
        if cont+1 <= numero:
            calculo = calculo*(cont+1)
        cont+=1
    return calculo

n=int(input("Dime un numero: "))
print(factorial(n))