'''
Ejercicio 12

Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es el día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.

'''

precioDia = 3.49
precioNoDia = 3.49*0.6

barrasVend = int(input("Cuantas barras has vendido que no son del dia: "))

print(f"El precio normal es {precioDia}, con el descuento cada barra vale {precioNoDia}. El beneficio del dia ha sido {barrasVend*precioNoDia}.")












