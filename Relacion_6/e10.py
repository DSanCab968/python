'''
Ejercicio 10

Escribir un programa que permita gestionar la base de datos de clientes de una
empresa. Los clientes se guardarán en un diccionario en el que la clave de cada
cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre,
dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se
trata de un cliente preferente. El programa debe preguntar al usuario por una opción
del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4)
Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la
opción elegida el programa tendrá que hacer lo siguiente:

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a
la base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y
nombre.
6. Terminar el programa.

'''
# Diccionario principal de clientes: {NIF: {datos_cliente}}
clientes = {}

def mostrar_datos_cliente(nif):
    """Muestra los datos de un cliente dado su NIF."""
    cliente = clientes.get(nif)
    if cliente:
        print(f"\nDatos del cliente {nif}:")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Preferente: {'Sí' if cliente['preferente'] else 'No'}\n")
    else:
        print("Cliente no encontrado.\n")

while True:
    print("Menú:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")

    opcion = input("Elige una opción (1-6): ").strip()

    if opcion == "1":
        # Añadir cliente
        nif = input("Introduce el NIF del cliente: ").strip()
        if nif in clientes:
            print("Ese NIF ya existe en la base de datos.\n")
            continue
        nombre = input("Nombre: ").strip()
        direccion = input("Dirección: ").strip()
        telefono = input("Teléfono: ").strip()
        correo = input("Correo: ").strip()
        preferente_input = input("¿Es cliente preferente? (sí/no): ").strip().lower()
        preferente = True if preferente_input == 'sí' else False

        clientes[nif] = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'correo': correo,
            'preferente': preferente
        }
        print(f"Cliente {nombre} añadido correctamente.\n")

    elif opcion == "2":
        # Eliminar cliente
        nif = input("Introduce el NIF del cliente a eliminar: ").strip()
        if nif in clientes:
            del clientes[nif]
            print(f"Cliente {nif} eliminado correctamente.\n")
        else:
            print("Cliente no encontrado.\n")

    elif opcion == "3":
        # Mostrar cliente
        nif = input("Introduce el NIF del cliente a mostrar: ").strip()
        mostrar_datos_cliente(nif)

    elif opcion == "4":
        # Listar todos los clientes
        if clientes:
            print("\nLista de todos los clientes:")
            for nif, datos in clientes.items():
                print(f"NIF: {nif}, Nombre: {datos['nombre']}")
            print()
        else:
            print("No hay clientes en la base de datos.\n")

    elif opcion == "5":
        # Listar clientes preferentes
        preferentes = {nif: datos for nif, datos in clientes.items() if datos['preferente']}
        if preferentes:
            print("\nClientes preferentes:")
            for nif, datos in preferentes.items():
                print(f"NIF: {nif}, Nombre: {datos['nombre']}")
            print()
        else:
            print("No hay clientes preferentes.\n")

    elif opcion == "6":
        # Terminar
        print("Programa terminado.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.\n")

