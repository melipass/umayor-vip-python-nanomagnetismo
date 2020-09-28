# -*- coding: utf-8 -*-
# Ejercicio 1 Semana 7
"""
Crear una función que calcule cual es el número menor de dos números enteros
"""

def NumeroMenor(num1, num2):
    try:
        assert num1 < num2
        return num1
    except AssertionError:
        return num2
    except:
        print("Error de cálculo. Revisar valores.")
        return -1

print("Ingrese dos números a continuación para calcular el número menor.")
primerNumero = int(input("Ingrese el número 1: "))
segundoNumero = int(input("Ingrese el número 2: "))
print("El número menor es " + str(NumeroMenor(primerNumero, segundoNumero)) + ".")