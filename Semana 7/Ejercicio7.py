# -*- coding: utf-8 -*-
# Ejercicio 7
"""
 Escriba una función que tome un flotante x y retorne 2cos(x) − sin^2(x).
"""
import math

def FuncionACalcular(x):
    resultado = 2*math.cos(x) - (math.sin(x)*math.sin(x))
    resultadoEnCadena = str(resultado)
    return resultadoEnCadena

valor = float(input("Ingrese un valor x en radianes para calcular la función 2cos(x) − sin^2(x): "))
print(FuncionACalcular(valor))