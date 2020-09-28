# -*- coding: utf-8 -*-
# Ejercicio 3 Semana 7
"""
Construir una función que calcule el factorial de todos los elementos de una lista.
"""

def Factorial(lista):
    for x in lista:
        factorial = x
        while x != 1:
            x -= 1
            factorial *= x
        yield factorial
        
miLista = [3,10,5,9]
miListaFactorizada = Factorial(miLista)
for valor in miListaFactorizada:
    print(valor)