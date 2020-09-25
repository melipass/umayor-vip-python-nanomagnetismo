#Ejercicio 5:
"""
Escriba un programa que tome dos números y que conteste cuál es el menor y cuál el mayor o
que escriba que son iguales.
"""

print("Ingrese dos valores numéricos.")
try:
    numeros = [int(input("Valor 1: ")),int(input("Valor 2: "))]
    numeros.sort()
    if numeros[0] != numeros[1]:
        print("El número mayor es",numeros[1],"y el menor es",numeros[0],'.')
    else:
        print("Los números tienen el mismo valor.")
except:
    print('Ingresó un valor no numérico o no entero.')