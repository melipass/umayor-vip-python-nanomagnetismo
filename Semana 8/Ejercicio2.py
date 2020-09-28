# -*- coding: utf-8 -*-
# Ejercicio 2 Semana 8
"""
 Investigue como generar dos gráficas diferentes en el mismo código Python. Escriba un programa
que ilustre lo aprendido.
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

plt.show()