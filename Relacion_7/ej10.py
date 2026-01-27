'''
Ejercicio 10

Escribir una función que convierta un número decimal en binario y otra que convierta
un número binario en decimal

'''

def fn_decToBin(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    return binario


def fn_binToDec(b):
    b = str(b)
    decimal = 0
    potencia = len(b) - 1

    for digito in b:
        decimal += int(digito) * (2 ** potencia)
        potencia -= 1

    return decimal


print(fn_decToBin(25))    # 11001
print(fn_binToDec(11001)) # 25
