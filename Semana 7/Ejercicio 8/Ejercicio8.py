# -*- coding: utf-8 -*-
# Ejercicio 8 semana 7
"""
Separe las funciones creadas en tareas anteriores en tr´ es módulos diferentes. Escriba un progra-
ma que incluya los tres módulos, cada uno utilizando una forma de import diferente (normal,
abreviado, importar función directamente), y haga uso de las funciones de cada módulo.
"""
import modulo1
import modulo2 as m2
from modulo3 import GenerarTresNumeros

#forma normal
print("A continuación devolveré el número menor entre -10 y 10: ")
print("El número menor es " + str(modulo1.NumeroMenor(-10, 10)) + ".")

#forma abreviada
print("Ahora transformaré 20 euros en dólares: ")
euros = 20
dolares = m2.ConvertirEURaUSD(euros)
print("El valor en dólares es USD$" + f"{dolares:.2f}")
    
#forma directa
print("Por último, generaré tres números al azar entre 0 y 100, que son los siguientes: ")
for x in GenerarTresNumeros():
    print(x)