import numpy as np
import tensor_operators
import generator
import animator

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
ani.ArrowAnimation(op.Ferromagnetism(0), 0)
ani.ArrowAnimation(op.Ferromagnetism(np.pi), 30)
ani.ArrowAnimation(op.Ferromagnetism(0), 60)
ani.ArrowAnimation(op.Ferromagnetism(np.pi/2), 90)
ani.ArrowAnimation(op.Ferromagnetism(3*np.pi/2), 120)
ani.ArrowAnimation(op.Paramagnetism(), 150)
