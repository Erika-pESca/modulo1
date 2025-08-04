#ejercio 1 calculadpra de indice de masa corporal
'''
 es una calculadora para medir su IMC
'''
peso = float(input("digite su peso: "))
altura = float(input("digite su altura: "))


imc = peso / (altura * altura)
"""
esta operacion nos ayuda a saber su indice de masa corporal 

args: 
peso (float): primera medidaa
altura (float): segunda medida

returns: 
float: es la divison y la potenciacion de nuestras dos variables 

"""

print(f"su imc: {imc:.2f}")
