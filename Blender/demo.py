import bpy, bmesh, random
import generator

"""
So far, by writing this code, I have seen the following hierarchy:
    context -> window -> scene -> collection -> objects -> meshes
"""

# variables
spins = [3,0,0] # number of spins
er = 5 # electron radius
dbs = 2 # distance between spins

demo1D = generator.Generator(spins,er,dbs)
demo1D.ClearScene()
demo1D.Create1DSpinsArray()