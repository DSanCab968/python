'''

Ejercicio 5

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.

'''
cantidad = abs(float(input("Dime la cantidad a invertir: ")))
interes = abs(float(input("Dime el interes anual: ")))
duracion = abs(int(input("Dime cuantos años durara la inversion: ")))
numYear = 1

for i in range(1, duracion + 1):
    dinero = cantidad * (1 + interes / 100) ** i
    print(f"El capital en {numYear} año es: {dinero:.2f} €")
    numYear += 1
