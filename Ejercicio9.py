'''
Ejercicio 9

Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión.

'''

capital=float(input("Introduzca el capital inicial: "))
tasaInteres=float(input("Introduzca tasa interes: "))
tiempo=float(input("Introduzca el tiempo: "))
interesFinal=float(capital*((tasaInteres/100)*tiempo))

print(f"El interes es: {interesFinal}")