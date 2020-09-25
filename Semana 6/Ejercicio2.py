# Ejercicio 3
"""
 Un zoológico cobra la entrada de admisión dependiendo de la edad del visitante: los ni˜ nos entre
3 y 12 a˜ nos pagan $10,000, los aultos mayores de 65 pagaran $13,000 y el resto pagara $16,000.
Cree un programa que lea, una por una, las edades de un grupo de visitantes. El usuario debe
introducir la linea ’fin’ para indicar que ya terminó de capturar los datos. Una vez que el
usuario haya terminado, el programa debe mostrar el total a pagar por el grupo.
"""

tarifaNormal = 16000
tarifaNiño = 10000
tarifaAdultoMayor = 13000
listaVisitantes = []

class Visitante:
    def __init__(self):
        edad = 0
        
def IngresarVisitantesFor():
    for x in range(1,int(cantidadVisitantes)+1):
        edadIngresada = input("Ingresar edad de visitante " + str(x) + ": ")
        globals()["Visitante " + str(x)] = Visitante()
        globals()["Visitante " + str(x)].edad = int(edadIngresada)
        listaVisitantes.append(globals()["Visitante " + str(x)])

def SumaPrecioFor(listaVisitantes):
    precioTotal = 0
    for visitante in listaVisitantes:
        if visitante.edad < 3:
            precioTotal += 0
        elif visitante.edad <= 12:
            precioTotal += tarifaNiño
        elif visitante.edad >= 65:
            precioTotal += tarifaAdultoMayor
        else:
            precioTotal += tarifaNormal
    print("El precio total es: ",str(precioTotal))

def IngresarVisitantesWhile():
    y = 0
    while (y != int(cantidadVisitantes)):
        edadIngresada = input("Ingresar edad de visitante " + str(y+1) + ": ")
        globals()["Visitante " + str(y+1)] = Visitante()
        globals()["Visitante " + str(y+1)].edad = int(edadIngresada)
        listaVisitantes.append(globals()["Visitante " + str(y+1)])
        y += 1
        
def SumaPrecioWhile():
    precioTotal = 0
    z = 0
    while z != len(listaVisitantes):
        if listaVisitantes[z].edad < 3:
            precioTotal += 0
        elif listaVisitantes[z].edad <= 12:
            precioTotal += tarifaNiño
        elif listaVisitantes[z].edad >= 65:
            precioTotal += tarifaAdultoMayor
        else:
            precioTotal += tarifaNormal
        z += 1
    print("El precio total es: ",str(precioTotal))


metodo = input("¿Desea calcular precio usando For (1) o usando While (2)?"
               + "\nIngrese el nombre o número correspondiente: ").lower()
if metodo == "for" or metodo == "1":
    cantidadVisitantes = input("¿Cuántas personas hay en este grupo de visitantes?: ")
    IngresarVisitantesFor()
    SumaPrecioFor(listaVisitantes)
elif metodo == "while" or metodo == "2":
    cantidadVisitantes = input("¿Cuántas personas hay en este grupo de visitantes?: ")
    IngresarVisitantesWhile()
    SumaPrecioWhile()
else:
    print("Vuelva a intentarlo.")