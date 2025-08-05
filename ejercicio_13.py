#mini sistema dde gestion de inventario
lista = {}


def agregar_producto(nombre, precio, cantidad):
    """
        Este programa gestiona un inventario de producto
        Permite agregar productos, realizar ventas y mostrar el inventario.
        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            cantidad (int): Cantidad del producto en inventario.

        Returns:
            str: Mensaje de confirmación al agregar el producto.
    """
    producto = {
        "nombre": nombre.lower(),
        "precio": precio,
        "cantidad": cantidad
    }
    lista.append(producto)
    print(f"El producto '{producto}' ha sido agregado.")

def realizar_venta(nombre, cantidad_vendida):
    """
    Este programa gestiona un inventario de producto
    Permite agregar productos, realizar ventas y mostrar el inventario.
    Args:
        nombre (str): Nombre del producto a vender.
        cantidad_vendida (int): Cantidad del producto a vender.
    Returns:
        str: Mensaje de confirmación al realizar la venta o error si no hay stock.
    """

    for producto in lista:
        if producto["nombre"] == nombre.lower():
            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] -= cantidad_vendida
                total = producto["precio"] * cantidad_vendida
                print(f"Venta realizada: {cantidad_vendida} unidades de '{producto['nombre']}' a {producto['precio']} cada una, el precio  es: {total}.")
            else:
                print(f"No hay suficiente stock de '{producto['nombre']}'. Stock actual: {producto['cantidad']}")
            return
    print(f"El producto '{nombre}' no se encuentra en el inventario.")

def mostrar_inventario():
    """
    Muestra el inventario de productos.
    Args:
      None
    Returns:
      str: Lista de productos en el inventario o mensaje si está vacío.
    """
    if not lista:
        print("El inventario está vacío.")
    else:
        print("\n--- Inventario ---")
        for producto in lista:
            print(f"Nombre: {producto['nombre'].capitalize()}, "
                  f"Precio: ${producto['precio']:.2f}, "
                  f"Cantidad: {producto['cantidad']}")
        print("-------------------------")

while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Ingrese su opción (1-4): ")
    match opcion:
     case "1":
         agregar_producto(
             input("Ingrese el nombre del producto: "),
             float(input("Ingrese el precio del producto: ")),
             int(input("Ingrese la cantidad del producto: "))
         )
     case "2":
         realizar_venta(
             input("Ingrese el nombre del producto a vender: "),
             int(input("Ingrese la cantidad a vender: "))
         )
     case "3":
         mostrar_inventario()
     case "4":
         print("Saliendo del sistema de inventario...")

     case _:
         print("Opción inválida. Por favor, ingrese un número del 1 al| 4.")

