'''
Ejercicio 1

Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
símbolo o un mensaje de aviso si la divisa no está en el diccionario.

'''

dinero = {
    "Euro":"€",
    "Dollar":"$",
    "Yen":"¥"
}

moneda = input("Que moneda quieres: ")

if moneda in dinero:
    print(f"El símbolo del {moneda} es {dinero[moneda]}")
else:
    print("No tenemos esa moneda")
  