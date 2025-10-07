#nombre=input(f"Dime tu nombre: ")
#print("Te voy a tocar " + nombre)

#Suma de dos numeros
'''
numero1=input("Dime un numero: ")
numero2=input("Dime otro numero: ")
resultado = float(numero1) + float(numero2)
print("El resultado es: " + str(resultado))

'''

#Calcular IMC
'''
peso=input("Dime tu peso en kg: ")
altura=input("Dime tu altura en metros: ")
imc = float(peso) / (float(altura)**2)
print(f"Tu IMC es: {imc}")

'''
#cALCULAR AREA Y PERIMETRO RECTANGULO
'''
base=float(input("Dime la medida de la base: "))
altura=float(input("Dime la altura: "))
area=float(base*altura)
perimetro=float(base+altura)*2
'''
#Normal
#print("El area es:  " + str(area))
#print("El perimetro es: "+str(perimetro))

#Format --- \n es para meter un salto de linea

#print(f"El area es: {area} \nEl perimetro es: {perimetro} ")

#Le damos el descuento y el precio y me da el percio con la rebaja hecha
'''
precio=float(input("Precio estandar: "))
descuento=float(input("Descuento a aplicar: "))
precioRebajado=float(precio-(precio*(descuento/100))) #No hacen falta parentesis

print(f"El precio rebajado es: {precioRebajado}")
'''

#Calcular interes simple

capital=float(input("Introduzca el capital inicial: "))
tasaInteres=float(input("Introduzca tasa interes: "))
tiempo=float(input("Introduzca el tiempo: "))
interesFinal=float(capital*((tasaInteres/100)*tiempo))

print(f"El interes es: {interesFinal}")

