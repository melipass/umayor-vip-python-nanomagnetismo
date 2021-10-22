import numpy
import os
import json

matrices = []
for i in range(len(os.listdir('out/'))):
    matrices.append(numpy.loadtxt('out/matrix-{}.txt'.format(i), delimiter=","))

config = json.load(open('config.json'))
print(config['keyframes'][0])