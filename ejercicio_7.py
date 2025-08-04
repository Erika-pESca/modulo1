# Lista de compras interactiva
lista = []
'''
programa que nos ayuda a agendar una lista podemos agregar, eliminar, listar productos y salir'''

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Listar productos")
    print("4. Salir")

    opcion = input("Ingrese su opción (1-4): ")

    def agenda ():
        """
        lista = [] es un diccionario donde podemos interartuar con el con lo que el usuario
        va agregar, eliminar y listar


        :return:
        opcion = nos va dirifir a la opcion que el usuario haya agregado
        y va cumplir su condicion
        """

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        lista.append(producto)
        print(f"El producto '{producto}' ha sido agregado.")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto que desea eliminar: ")
        if producto in lista:
            lista.remove(producto)
            print(f" El producto '{producto}' ha sido eliminado.")
        else:
            print(f"El producto '{producto}' no se encuentra en la lista.")

    elif opcion == "3":
        print("\n LISTA DE COMPRAS:")
        if not lista:
            print("La lista está vacía.")
        else:
            for i, producto in enumerate(lista, start=1):
                print(f"{i}. {producto}")

    elif opcion == "4":
        print(" Saliendo")
        break

    else:
        print(" Opción inválida. Por favor, ingrese un número del 1 al 4.")
