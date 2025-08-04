#tabla de multiplicar
numero = int(input("Ingrese un numero: "))
contador = 0
'''
 es un programa para tablas de multiplicar 
'''

def verificar_multiplicar(numero):
 """
for: recibe un numero y recorre ese numero en el rango del 1 a 10

args:
 numnero es almacenado en resultado en contenedor para que cumpla el rango del 1 a 10
 resultado: es la multiplicacion de numero con contador
"""
for i in range(0, 10):
    contador += 1
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")

