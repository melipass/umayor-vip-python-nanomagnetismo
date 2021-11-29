import numpy as np
import tensor_operators
import generator
import animator
import stage
import os
import json

"""
    context -> window -> scene -> collection -> objects -> meshes
"""
# loading matrices
matrices = []
folder = os.path.dirname(os.path.realpath(__file__))[:-14] + 'matrices\\'
print(folder)
for i in range(len(os.listdir(folder))):
    matrices.append(np.loadtxt(folder + 'matrix-{}.txt'.format(i), delimiter=","))

# load config
config = json.load(open(folder[:-10] + '\\src\\config.json'))

# variables
spins = [len(matrices[0]), len(matrices[0][0]), 1]  # spin rows per axis (x,y,z)
er = 4  # electron radius
dbs = 3  # distance between spins

# classes
gen = generator.Generator(spins, er, dbs)
gen.ClearScene()
gen.Create3DSpinsArray()
op = tensor_operators.TensorOperators(spins)
ani = animator.Animator(spins)
ani.ClearAnimations()


i = 0
keyframe = config['keyframes'][i]
delta = config['delta'][0]
for matrix in matrices:
    print(matrix)
    try:
        ani.ArrowAnimation(op.AutomataMatrix(matrix), config['keyframes'][i],
                       delta = config['delta'][i], axis="z")
        keyframe = config['keyframes'][i]
        delta = config['delta'][i]
    except:
        keyframe += 30
        delta = 30
        ani.ArrowAnimation(op.AutomataMatrix(matrix), keyframe,
                       delta = delta, axis="z")
    i = i + 1









#  animation

# ani.ArrowAnimation(op.Ferromagnetism(0), 0, axis="x")
# ani.ArrowAnimation(op.Ferromagnetism(np.pi), 120, axis="x")
# ani.ArrowAnimation(op.Antiferromagnetism(0), 240, axis="x")
# ani.ArrowAnimation(op.Antiferromagnetism(np.pi), 360, axis="x")
# ani.ArrowAnimation(op.Paramagnetism(), 480, axis="x")
# ani.ArrowAnimation(op.Paramagnetism(), 480, axis="z")
# ani.ArrowAnimation(op.Paramagnetism(), 600, axis="x")
# ani.ArrowAnimation(op.Paramagnetism(), 600, axis="z")
# ani.ArrowAnimation(op.OperationMatrix(), 640, axis="x")
# ani.ArrowAnimation(op.OperationMatrix(), 640, axis="z")

#stage = stage.Stage()