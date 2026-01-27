'''

Ejercicio 9

Escribir una función que calcule el máximo común divisor de dos números y otra que
calcule el mínimo común múltiplo

'''

def mcd(a, b):
  
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
  
    return a * b // mcd(a, b)

resultado = mcd(3, 7)
resultado2 = mcm(88, 65)

print("MCD de 3 y 7:", resultado)
print("MCM de 88 y 65:", resultado2)



