'''

Ejercicio 8

Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

'''
#con 2 for

numOcurr = abs(int(input("Dime un número: ")))

for i in range(1, numOcurr + 1):
    for j in range(i, 0, -1):
        print(2*j - 1, end=" ")
    print()

'''
#con for y array

numOcurr = abs(int(input("Dime un número: ")))

for i in range(1, numOcurr + 1):
    fila = [] 
    for j in range(i, 0, -1):
        fila.append(2*j - 1)
    print(fila)
'''
    


'''
Forma incompleta:

numOcurr = abs(int(input("Dime un numero: ")))

x = 1
arr=[]

for i in range(0,numOcurr):
    arr.append(x)
    arr.reverse()

    print(arr)
    x += 2
'''






    