#Ejercicio 1
"""
 Escriba un programa que tome 3 números y los imprima en pantalla de menor a mayor.
"""

print("Ingrese tres números para ordenar de menor a mayor.")
try:
    numeros = [int(input("Número 1: ")),int(input("Número 2: ")),
            int(input("Número 3: "))]
    numeros.sort()
    print("En orden quedan así:")
    for x in numeros:
        print(x)
except:
    print("El valor ingresado no es un número entero.")