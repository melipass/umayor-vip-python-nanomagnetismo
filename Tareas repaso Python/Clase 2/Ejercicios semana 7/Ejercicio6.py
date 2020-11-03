# -*- coding: utf-8 -*-
# Ejercicio 6 semana 7
"""
Investigue como generar números aleatorios en Python y cree una función que retorne tr´ es
números aleatorios entre 0 y 100.
"""
from random import randint

def GenerarTresNumeros():
    uno = randint(0,100)
    dos = randint(0,100)
    tres = randint(0,100)
    return [str(uno), str(dos), str(tres)]

print("En este programa se entregan tres números entre 0 y 100, que son los siguientes: ")
for x in GenerarTresNumeros():
    print(x)