import numpy
import os

matrices = []
for i in range(len(os.listdir('../Automata/out/'))):
    matrices.append(numpy.loadtxt('../Automata/out/matrix-{}.txt'.format(i), delimiter=","))

print(matrices)