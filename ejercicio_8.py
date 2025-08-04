#validacion de palindromos

palabra_original = input("Ingrese una palabra: ")
palabra = palabra_original.replace(" ", "")  # Elimina los espacios en blanco

def polinomio(palabra):
    """verifica si una frase es un palindromo o no
    Un palíndromo es una palabra o frase que se lee igual hacia adelante y hacia atrás,
    ignorando los espacios y sin importar mayúsculas o minúsculas.

     Args:
        palabra_original (str): Palabra o frase
        palabra = sea igual que la palabra_original elimina los espacios
        invertido = "" Variable para almacenar el texto invertido
         Luego, se recorre la palabra original desde el último carácter hasta el primero
         utilizando un bucle for con índices en reversa.
         En cada iteración, se agrega el carácter actual a la variable 'invertido'.


    Returns:
        bool: True si es un palíndromo, False si no lo es.
     """


invertido = ""
for i in range(len(palabra) - 1, -1, -1):  # 0 hasta 4
    invertido = invertido + palabra[i]

if invertido == palabra:
    print(f"{palabra_original} es un palíndromo")
else:
    print(f"{palabra_original} no es un palíndromo")
