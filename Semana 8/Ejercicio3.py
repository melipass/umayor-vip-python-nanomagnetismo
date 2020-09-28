# -*- coding: utf-8 -*-
# Ejercicio 3 Semana 8
"""
  Investigue como nombrar los ejes x e y en las gráficas. Escriba un código Python ilustrando lo
aprendido.
"""
import matplotlib.pyplot as plt
import numpy as np

xi = 0
xf = 2 * np.pi
nx = 200
x = np.linspace(xi, xf, nx)
y = 2 * np.cos(x) - (np.sin(x) * np.sin(x))

plt.plot(x,y)

y = -x
plt.plot(x,y)

plt.xlabel("Eje x")
plt.ylabel("Eje y")

plt.show()