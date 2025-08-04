#ejercio  de verificador de mayor de edad

'''
es un programa donde nos verifica si somos mayor de edad y menor de edad
'''
edad = int(input("Ingrese su edad: "))
def verificar_edad(edad):
    """
    esta funcion nos ayuda a evaluar condiciones

    args:
      edad: es nuestra variable
      if:Nos deja el valor de edad, para saber cuando es recien nacido

      elif: nos ayuda a validar si el if no se cumple pasa a elif a validar una condicion

      else: cierra el ciclo de elif
    """
if edad ==0:
    print(f"usted es recien nacido ")

elif edad > 18:
    print(f"usted es mayor de edad ")
elif edad < 18:
    print(f"usted es menor de edad ")
else:
    print(f"invalido")


