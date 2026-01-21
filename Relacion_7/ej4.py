'''
Ejercicio 4

Escribir una función que calcule el total de una factura tras aplicarle el IVA. La
función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el
total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá
aplicar un 21%.

'''

dinero=int(input("Dime la cantidad de petrodolares: "))
ivaPer= int(input("Dime el IVA a aplicar en %: "))
iva = ivaPer/100

def IVA(dinero,iva = 0.21):
    total=0
    total=dinero+(dinero*iva)
    
    return(total)
    
# si no le ponemos el iva, pilla el valor default
result=IVA(dinero)
print(result)
      