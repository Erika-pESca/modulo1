# Adivina el número
import random
"""
programa de juego adivina el numero secreto del 1 a 100 y el usuario tiene 5 intentos 
"""

numero_secreto = random.randint(1, 100)
intentos = 5
adivinado = False


print("Adivina el número secreto entre 1 y 100. Tienes 5 intentos.")
def adivinar():
    """
    juego en que el usuario debe adivinar un numero del grango del 1 a 100, el usuario tiene 5 intentos

    Args:
        numero_secreto= un numero aleatorio entre 1 y 100
        intentos= 5 intentos que tiene el usuario debe adivinar
        adivinado= variable que nos permite finalizar el ciclo si el usuario adivino o no
    Returns:
    pide ala usuario un numero

     if: nos va decir si el numero que ingreso es mayor o menor que el numero secreto
     else: nos va digitar un mensaje si el usuario adivina el numero secreto
    """

while intentos > 0:
    numero = int(input("Ingrese un número: "))

    if numero > numero_secreto:
        print("El número es mayor que el número secreto.")

    elif numero < numero_secreto:
        print("El número es menor que el número secreto.")

    else:
        print("¡Felicidades! Adivinaste el número secreto.")
        adivinado = True
        break

    intentos -= 1

if not adivinado:
    print(f"Lo siento. El número secreto era {numero_secreto}.")
