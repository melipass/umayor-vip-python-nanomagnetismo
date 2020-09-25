#Ejercicio 3
"""
En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido en el
lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
 Si los tres dados son seis, mostrar el mensaje “Excelente”.
 Si dos dados se obtiene seis, mostrar el mensaje “Muy bien”.
 Si un dado se obtienen seis, mostrar el mensaje “Regular”.
 Si ningún dado se obtiene seis, mostrar el mensaje “P´ esimo”.
Utilize combinaciónes de condiciones (and y or) solamente.
"""
from random import randint

dados = []

def LanzarDados(cantidadDeDados):
    print("Sus dados son:")
    i=0
    while i != cantidadDeDados:
        dado = randint(1,6)
        i += 1
        print("Dado " + str(i) + ": " + str(dado))
        dados.append(dado)

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