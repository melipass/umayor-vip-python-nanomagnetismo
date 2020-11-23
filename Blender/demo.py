import bpy, bmesh, random
import numpy as np
import tensor_operators, generator, rotator

"""
So far, by writing this code, I have seen the following hierarchy:
    context -> window -> scene -> collection -> objects -> meshes
"""

# variables
spins = [5,5,1] # spin rows per axis (x,y,z)
er = 5 # electron radius
dbs = 7 # distance between spins

# classes
gen = generator.Generator(spins,er,dbs)
gen.ClearScene()
gen.Create3DSpinsArray()

rot = rotator.Rotator(spins)

op = tensor_operators.TensorOperators(spins)

# scene set-up

op.Ferromagnetism(np.pi/2)
#op.Antiferromagnetism(np.pi)
#op.Paramagnetism()

rot.CollectionRotator(op.spins_tensor,"X")
#rot.CollectionRotator(op.spins_tensor,"Y")
