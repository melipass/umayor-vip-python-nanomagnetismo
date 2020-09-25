#Ejercicio 4
"""
Repita el ejercicio 3 usando solamente if anidados.
"""
from random import randint
from sys import exit

dados = []

def LanzarDados(cantidadDeDados):
    print("Sus dados son:")
    i=0
    while i != cantidadDeDados:
        dado = randint(1,6)
        i += 1
        print("Dado " + str(i) + ": " + str(dado))
        dados.append(dado)

#Código antiguo:
"""
try:
    LanzarDados(3)
    if dados[0] == 6 and dados[1] == 6 and dados[2] == 6:
        print("Excelente.")
    elif (dados[0] == 6 and dados[1] == 6
    or dados[1] == 6 and dados[2] == 6
    or dados[0] == 6 and dados[2] == 6):
        print("Muy bien.")
    elif dados[0] == 6 or dados[1] == 6 or dados[2] == 6:
        print("Regular.")
    else:
        print("Pésimo.")
except:
    print("Error.")
"""

#Código nuevo:
LanzarDados(3)
if dados[0] == 6:
    if dados[1] == 6:
        if dados[2] == 6:
            print("Excelente.")
            exit()
        print("Muy bien.")
        exit()
    elif dados[2] == 6:
        print("Muy bien.")
        exit()
    print("Regular.")
    exit()
elif dados[1] == 6:
    if dados[2] == 6:
        print("Muy bien.")
        exit()
    print("Regular.")
    exit()
elif dados[2] == 6:
    print("Regular.")
    exit()
print("Pésimo.")
exit()