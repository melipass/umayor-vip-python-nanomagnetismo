# -*- coding: utf-8 -*-
# Ejercicio 1 semana 8
"""
Utilizando Python, obtenga la gráfica de la función
y = 2cos(x)−sin^2(x) para 0 < x < 2π. Utilize
el numero π definido en numpy.
"""
import matplotlib.pyplot as plt
import numpy as np

xi = 0
xf = 2 * np.pi
nx = 200
x = np.linspace(xi, xf, nx)
y = 2 * np.cos(x) - (np.sin(x) * np.sin(x))

plt.plot(x,y)
plt.show()