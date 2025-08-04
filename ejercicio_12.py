# conversor de unidades
factores_conversion = {
    "metros": 1.0,
    "pies": 3.28084,
    "kilometros": 0.001,
    "centimetros": 100.0,
    "milimetros": 1000.0,
    "pulgadas": 39.3701
}

def convertir_unidad(cantidad, unidad_origen, unidad_destino):
    """
    Convierte una cantidad de una unidad a otra usando factores de conversión desde metros.

    Args:
        cantidad (float): La cantidad a convertir.
        unidad_origen (str): La unidad de la cantidad original.
        unidad_destino (str): La unidad a la que se desea convertir.

    Returns:
        float: La cantidad convertida si las unidades son válidas.
        str: Mensaje de error si alguna unidad no es válida.
    """
    if unidad_origen not in factores_conversion:
        return f"Error: la unidad de origen '{unidad_origen}' no está disponible."

    if unidad_destino not in factores_conversion:
        return f"Error: la unidad de destino '{unidad_destino}' no está disponible."

    cantidad_en_metros = cantidad / factores_conversion[unidad_origen]

    resultado = cantidad_en_metros * factores_conversion[unidad_destino]

    return resultado

cantidad = float(input("Ingrese la cantidad: "))
origen = input("Unidad de origen (metros, pies, kilometros, etc.): ").lower()
destino = input("Unidad de destino (metros, pies, kilometros, etc.): ").lower()

conversion = convertir_unidad(cantidad, origen, destino)

if isinstance(conversion, str):
    print(conversion)
else:
    print(f"{cantidad} {origen} equivale a {conversion:.4f} {destino}")
