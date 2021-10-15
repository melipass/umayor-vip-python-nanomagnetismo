import numpy as np
import tensor_operators
import generator
import animator
import stage
import os

"""
    context -> window -> scene -> collection -> objects -> meshes
"""
# variables
spins = [4, 4, 1]  # spin rows per axis (x,y,z)
er = 3  # electron radius
dbs = 6  # distance between spins

# classes
gen = generator.Generator(spins, er, dbs)
gen.ClearScene()
gen.Create3DSpinsArray()
op = tensor_operators.TensorOperators(spins)
ani = animator.Animator(spins)
ani.ClearAnimations()

matrices = []
folder = os.path.dirname(os.path.realpath(__file__))[:-13] + 'out\\'
for i in range(len(os.listdir(folder))):
    matrices.append(np.loadtxt(folder + 'matrix-{}.txt'.format(i), delimiter=","))

i = 0
for matrix in matrices:
    print(matrix)
    ani.ArrowAnimation(op.AutomataMatrix(matrix), i, axis="x")
    i = i + 60

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
