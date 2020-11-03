# -*- coding: utf-8 -*-
# Ejercicio 4
"""
Desarrollar un programa con las siguientes caracter´ısticas:
• Tome un valor entero impar comprendido entre 1 y 35.
• Calcule la serie num´ erica 1 + 3 + 5 + ··· + n.
• Calcule 1 * 3 * 5 * ··· * n.
• Retorne el resultado de ambos cálculos.
"""
import sys

def GenerarSerieImpares(n):
    try:
        assert n % 2 == 1
    except AssertionError:
        sys.exit("Error: El número no es par")
    i = 1
    yield i
    while i != n:
        i += 2
        yield i
 
def ImprimirSerieImpares(n, operador):
    valores = list(GenerarSerieImpares(n))
    for x in valores[:-1]:
        print(str(x) + " " + operador + " ", end="")
    print(valores[-1])
    return
            
def CalcularSuma(n):
    valores = list(GenerarSerieImpares(n))
    i = 0
    for x in valores:
        i += x
    return i

def CalcularMultiplicacion(n):
    valores = list(GenerarSerieImpares(n))
    i = 1
    for x in valores:
        i *= x
    return i

numero = int(input("Ingrese un valor impar entre 1 y 35: "))
if numero >= 1 and numero <= 35:
    ImprimirSerieImpares(numero, "+")
    print(CalcularSuma(numero))
    ImprimirSerieImpares(numero, "*")
    print(CalcularMultiplicacion(numero))
else:
    print("Error: El número está fuera del rango o es un valor inválido.")