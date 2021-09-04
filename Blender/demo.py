import numpy as np
import tensor_operators
import generator
import animator
import stage

"""
    context -> window -> scene -> collection -> objects -> meshes
"""
# variables
spins = [5, 1, 1]  # spin rows per axis (x,y,z)
er = 3  # electron radius
dbs = 6  # distance between spins

# classes
gen = generator.Generator(spins, er, dbs)
gen.ClearScene()
gen.Create3DSpinsArray()
op = tensor_operators.TensorOperators(spins)
ani = animator.Animator(spins)
ani.ClearAnimations()

#  animation

ani.ArrowAnimation(op.Ferromagnetism(0), 0, axis="x")
ani.ArrowAnimation(op.Ferromagnetism(np.pi), 120, axis="x")
ani.ArrowAnimation(op.Antiferromagnetism(0), 240, axis="x")
ani.ArrowAnimation(op.Antiferromagnetism(np.pi), 360, axis="x")
ani.ArrowAnimation(op.Paramagnetism(), 480, axis="x")
ani.ArrowAnimation(op.Paramagnetism(), 480, axis="z")
ani.ArrowAnimation(op.Paramagnetism(), 600, axis="x")
ani.ArrowAnimation(op.Paramagnetism(), 600, axis="z")

stage = stage.Stage()
