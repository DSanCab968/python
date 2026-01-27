# diccionario que traduca de ingles a español 

dic = {'hello':'hola'}

while True:
    print("1. Mostrar el diccionario")
    print("2. Añadir elemento")
    opcion = int(input("Dime la opcion que deseas: "))

    if opcion == 1:
        print(dic)

    elif opcion == 2:
        elemento = input("Dime el elemento que desas añadir: ")
        valor = input("Dime el valor que tendra:")
        dic[elemento] = valor
    else:
        break

    