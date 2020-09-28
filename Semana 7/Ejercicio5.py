# -*- coding: utf-8 -*-
# Ejercicio 5
"""
Escriba una función que transforme un número del 0 al 999 a números romanos.
"""

def TransformarANumerosRomanos(numero):
    centenas = numero // 100
    centenasRomanas = ["C", "D", "M"]
    decenas = (numero - centenas*100) // 10
    decenasRomanas = ["X", "L", "C"]
    unidades = numero - centenas*100 - decenas*10
    unidadesRomanas = ["I", "V", "X"]
    numeroADevolver = (ArmarNumero(centenas, centenasRomanas)
                       + ArmarNumero(decenas, decenasRomanas)
                       + ArmarNumero(unidades, unidadesRomanas))
    return numeroADevolver
        
def ArmarNumero(numero, letras):
    if numero == 9:
        return letras[0] + letras[2]
    elif numero == 4:
        return letras[0] + letras[1]
    elif numero == 5:
        return letras[1]
    elif numero < 4:
        return letras[0] * numero
    else:
        numero -= 5
        return letras[1] + letras [0] * numero


print(TransformarANumerosRomanos(784))