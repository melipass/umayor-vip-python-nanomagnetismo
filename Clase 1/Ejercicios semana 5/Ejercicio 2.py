# Ejercicio 2
"""
Escriba un programa que genere la tabla de multiplicar (del 1 al 10) de un número dado.
"""

n = int(input("Ingrese el número para calcular su tabla: "))
y = 0

for x in range(1,13):
    print(str(n) + " x " + str(x) + " = " + str(n*x))
    
while y != 12:
    y += 1
    print(str(n) + " x " + str(y) + " = " + str(n*y))