# -*- coding: utf-8 -*-
import numpy as np
import array_to_latex as a2l # https://pypi.org/project/array-to-latex/
    
ImprimirLaTeX = lambda A : print(a2l.to_ltx(A))
# Vector de 1 dimensión a LaTeX
vec1 = np.array([1,2,3,4])
print("A continuación se imprimirá el vector 1x4", str(vec1), "para insertar en LaTeX:")
ImprimirLaTeX(vec1)
"""
Devuelve:
    \begin{bmatrix}
      1.00 &  2.00 &  3.00 &  4.00
    \end{bmatrix}
"""

for i in range(0,4):
    vec1[i] = vec1[i]+1
print("\nAhora, al vector anterior le sumaré 1 a cada elemento:")
ImprimirLaTeX(vec1)    
"""
Devuelve:
    \begin{bmatrix}
      2.00 &  3.00 &  4.00 &  5.00
    \end{bmatrix}
"""

vec2=np.array([[3],[2],[1]])
print("\nLuego imprimiré un vector 3x1:")
ImprimirLaTeX(vec2)
"""
Devuelve:
    \begin{bmatrix}
      3.00\\
      2.00\\
      1.00
    \end{bmatrix}
"""

np.array([[65E-1,77.5642,3.322],
		[5.17,10E-2,3],
		[7.1,1.91123,53.3224]])

vec3=np.array([[65E-1,77.5642,3.322],
               [5.17,10E-2,3],
               [7.1,1.91123,53.3224]])
print("\nPor último, un vector 3x3 con decimales:")
ImprimirLaTeX(vec3)
"""
Devuelve:
    \begin{bmatrix}
      6.50 &  77.56 &  3.32\\
      5.17 &  0.10 &  3.00\\
      7.10 &  1.91 &  53.32
    \end{bmatrix}
"""

for i in range(0,3):
    for j in range(0,3):
        vec3[i][j] = vec3[i][j] * 2
print("\nY recorro cada elemento para multiplicarlo por 2:")
ImprimirLaTeX(vec3)
"""
Devuelve:
    \begin{bmatrix}
      13.00 &  155.13 &  6.64\\
      10.34 &  0.20 &  6.00\\
      14.20 &  3.82 &  106.64
    \end{bmatrix}
"""