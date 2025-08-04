#contador de frecuencia de palabras
frecuencia = {}

frase = input("Ingrese una frase: ")
def frecuencia(texto):
    """
    Esta funcion recibe un texto o una palabra y determina que cantidad de
    veces esta esa palabra en el texto.

    Args:
        texto (str): Texto que desea ser frecuencia
        palabras (list): Lista de palabras
        frecuencia (dic): Diccionario que contiene la frecuencia de las palabras

    Returns:
        La frecuencia de las palabras (dic)
        La cantidad de palabras(int)
"""
palabras = frase.lower()
frase = frase.split()


for palabra in frase:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    print(f"Frecuencia de palabras {palabra} ")
    for palabra, cantidad in frecuencia.items():
        print(f"{palabra}= {cantidad}")