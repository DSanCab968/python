'''

Ejercicio 12

Escribir un programa que almacene las matrices
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando
cada vector fila en una lista

'''

a = (
    (1, 2, 3),
    (4, 5, 6)
)

b = (
    (-1, 0),
    (0, 1),
    (1, 1)
)

c = [
    [0,0],
    [0,0]
]


for i in range(len(a)):# es 2
    for j in range(len(b[0])):#cojo las columnas de b q son 2
        for k in range(len(b)): # columnas de a entre filas de b
            c[i][j] += a[i][k] * b[k][j]
        
print(c)

        







