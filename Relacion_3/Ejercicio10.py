'''
Ejercicio 10

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

●​ Ingredientes vegetarianos: Pimiento y tofu.
●​ Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva.


'''

tipo = input("Quieres pizza vegetariana? [s/n]: ")

if tipo == "s":
    print("Tomate, mozzarella y: [pimiento o tofu]")
    ingredienteVeg = input("Elige: [pimiento/tofu]")
    print(f"La pizza es vegetariana y lleva tomate, mozzarella y {ingredienteVeg}.")
else:
    print("Tomate, mozzarella y: [peperoni, jamon, salmon]")
    ingredienteNoVeg = input("Elige: [peperoni/jamon/salmon]")
    print(f"La pizza no es vegetariana y lleva tomate, mozzarella y {ingredienteNoVeg}.")