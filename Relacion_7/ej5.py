'''
Ejercicio 5

Escribir una función que calcule el área de un círculo y otra que calcule el volumen
de un cilindro usando la primera función.

'''
import math

r=float(input("Dime el radio del circulo: "))
h=float(input("Dime la altura del cilindro: "))

def areaCirculo(radio):
    area = math.pi*(radio**2)
    return(area)

areaC=areaCirculo(r)

def volCil(alt,area):
    vol=alt*area
    return(vol)

volCilindro=volCil(h,areaC)

print(areaC)
print(volCilindro)

