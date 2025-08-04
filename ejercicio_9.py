# Agenda de contactos en el diccionario
contacto = {}

while True:
    print("\n MENU DE OPCIONES")
    print("1. añadir un contacto")
    print("2. buscar telefono")
    print("3. mostrar los contactos")
    print("4. salir")

    opcion = input("Ingrese una opcion: 1 a 4 ")
    def telefono(nombre, telefono):
        """
        este programa agenda contactos y perimite al usuario gestionar una agenda
         args :
         contacto{}= utiliza un diccionario para almacenar los nombres como claves y los telefonos como valores
        y el usuario puede interatuar en ella agregando, buscando y listando

        :return:
        entra al bucle y valida la opcion que haya escogido el usuario ya sea de agregar, buscando y listando
        """
    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto que desea ingresar: ")
        telefono = input("Ingrese el telefono del contacto que desea ingresar: ")
        contacto[nombre] = telefono
        print(f"Contacto '{nombre}' ha sido agregado.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        if nombre in contacto:
            print(f"El numero de {nombre} es: {contacto[nombre]}")
        else:
            print(f"El contacto '{nombre}' no existe.")

    elif opcion == "3":
        if not contacto:
            print("La agenda está vacía.")
        else:
            print("\n--- Contactos guardados ---")
            for nombre, telefono in contacto.items():
                print(f"{nombre}: {telefono}")

    elif opcion == "4":
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción inválida, por favor intente de nuevo.")
