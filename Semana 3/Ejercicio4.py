#Ejercicio 4:
"""
Escriba un programa que tome el a˜ no actual y un a˜ no cualquiera y que escriba cuántos a˜ nos han
pasado desde ese a˜ no o cuántos a˜ nos faltan para llegar a ese a˜ no.
"""

from datetime import datetime

añoActual = datetime.now().year
try:
    añoIngresado = int(input('Ingrese un año: '))
    if añoIngresado < añoActual:
        print('Han pasado',str(añoActual - añoIngresado),
              'años desde',str(añoIngresado),'.')
    elif añoIngresado > añoActual:
        print('Faltan',str(añoIngresado - añoActual),
              'para el',añoIngresado,'.')
    else:
        print("Ese es el año actual.")
except:
    print('Error: Entrada incorrecta.')