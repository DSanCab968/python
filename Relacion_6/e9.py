'''
Ejercicio 9

Escribir un programa que gestione las facturas pendientes de cobro de una
empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
factura será el número de factura y el valor el coste de la factura. El programa debe
preguntar al usuario si quiere añadir una nueva factura, pagar una existente o
terminar. Si desea añadir una nueva factura se preguntará por el número de factura
y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará
por el número de factura y se eliminará del diccionario. Después de cada operación
el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la
cantidad pendiente de cobro.

'''

facturas = {}

cobrado = 0

while True:
    print("\nOpciones:")
    print("1. Añadir nueva factura")
    print("2. Pagar factura")
    print("3. Terminar")
    
    opcion = input("Elige una opción (1/2/3): ").strip()
    
    if opcion == "1":
     
        numero = input("Introduce el número de la factura: ").strip()
        if numero in facturas:
            print("Esa factura ya existe.")
            continue
        while True:
            try:
                coste = float(input("Introduce el coste de la factura: "))
                break
            except ValueError:
                print("Introduce un número válido para el coste.")
        facturas[numero] = coste
        print(f"Factura {numero} añadida con coste {coste:.2f} €.")
        
    elif opcion == "2":
        
        numero = input("Introduce el número de la factura a pagar: ").strip()
        if numero in facturas:
            cobrado += facturas[numero] 
            del facturas[numero]          
            print(f"Factura {numero} pagada.")
        else:
            print("No existe esa factura.")
            
    elif opcion == "3":
     
        print("Programa terminado.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
        continue
    
    
    pendiente = sum(facturas.values())
    print(f"\nCantidad cobrada: {cobrado:.2f} €")
    print(f"Cantidad pendiente de cobro: {pendiente:.2f} €")
