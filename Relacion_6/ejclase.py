# diccionario que traduca de ingles a español para usar los metodos

dic = {'hello':'hola'}

while True:
    print("1. Mostrar el diccionario")
    print("2. Añadir elemento")
    print("3. Actualizar elemento")
    print("4. Borrar elemento")
    print("5. Mostrar claves")
    print("6. Mostrar valores")
    opcion = int(input("Dime la opcion que deseas: "))

    # mostrar
    if opcion == 1:
        print(dic)

    # añadir
    elif opcion == 2:
        elemento = input("Dime el elemento que desas añadir: ")
        valor = input("Dime el valor que tendra:")
        dic[elemento] = valor
    
    #actualizar
    elif opcion == 3:
        pActualizar = input("Dime la palabra en inlges para actualizar: ")
        nValor = input("Introduce un nuevo valor: ")
        dic[pActualizar] = nValor

    #borrar
    elif opcion == 4:
        pBorrar = input("Cual quieres borrar")
        del dic[pBorrar]
        print("Palabra eliminada")

    #mostrar keys
    elif opcion == 5:
        for op in dic.keys():
            print(op)

    #mostrar valores
    elif opcion == 6:
        for op in dic.values():
            print(op)

    else:
        break

