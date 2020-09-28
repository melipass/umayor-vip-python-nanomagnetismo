# -*- coding: utf-8 -*-
# Ejercicio 4 semana 8
"""
Modifique el código mostrado en el ejemplo 1 (gráfica y = x) para que muestre de manera
expl´ıcita los ejes x e y con sus respectivos nombres.
"""
import matplotlib.pyplot as plt
import numpy as np

xi = 0
xf = 2 * np.pi
nx = 200
x = np.linspace(xi, xf, nx)
y = 2 * np.cos(x) - (np.sin(x) * np.sin(x))

plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.plot(x,y)
plt.show()