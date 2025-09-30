'''
Ejercicio 11

Imagina que acabas de abrir una nueva cuenta de ahorros que
te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la
cuenta de ahorros, introducida por el usuario. Después el
programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales.

'''

tasaInteres = 0.04
dineroDepo = float(input("Dime cuanto dinero tienes en el banco: "))

dineroYear1 = dineroDepo + (dineroDepo*(tasaInteres))
dineroYear2 = dineroDepo + (dineroDepo*(tasaInteres*2))
dineroYear3 = dineroDepo + (dineroDepo*(tasaInteres*3))

print(f"En un año tendras {round(dineroYear1,2)} €")
print(f"En dos año tendras {round(dineroYear2,2)} €")
print(f"En tres año tendras {round(dineroYear3,2)} €")