import bpy, bmesh, random
import numpy as np
import tensor_operators, generator, rotator

"""
So far, by writing this code, I have seen the following hierarchy:
    context -> window -> scene -> collection -> objects -> meshes
"""

# variables
spins = [5,5,1] # spin rows per axis (x,y,z)
er = 3 # electron radius
dbs = 6 # distance between spins

# classes
gen = generator.Generator(spins,er,dbs)
gen.ClearScene()
gen.Create3DSpinsArray()

rot = rotator.Rotator(spins)

op = tensor_operators.TensorOperators(spins)

# scene set-up

op.Ferromagnetism(0)
#op.Antiferromagnetism(np.pi)
#op.Paramagnetism()

#rot.CollectionRotator(op.spins_tensor,"X",np.pi/2)
rot.CollectionRotator(op.spins_tensor,"Y",np.pi/2)