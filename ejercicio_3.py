#Contador de vocales y consonantes
'''
contador de vacales y consonantes
'''
frase= str(input("digite una frase: "))
vocales = 0
consonates = 0
def verificar_frase(frase):
    """
    esta funcion verifica cuantas vocales y consonantes hay en una frase

    args:
     frase: es nuestra variable
     vocales: es nuestra variable
     consonates: es nuestra variable

    for: hace el ciclo de verificar cuantas vocales y consonantes hay en una frase
    if: valida cuantas vocales y consonantes hay en una frase y las agrega al contador

    return: es la variable vocal y consonante
    """
for letra in frase:
    if letra in 'aeiou':

        vocales += 1
    else:
        consonates += 1


print(f"su frase es: {frase},\n tiene un total de vocales {vocales} \n consonantes de: {consonates}")





