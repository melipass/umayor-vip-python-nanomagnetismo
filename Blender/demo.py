import bpy, bmesh, random
import numpy as np
import tensor_operators, generator, rotator

"""
    context -> window -> scene -> collection -> objects -> meshes
"""

# variables
spins = [5,1,1] # spin rows per axis (x,y,z)
er = 3 # electron radius
dbs = 6 # distance between spins

# classes
gen = generator.Generator(spins,er,dbs)
gen.ClearScene()
gen.Create3DSpinsArray()

rot = rotator.Rotator(spins)

op = tensor_operators.TensorOperators(spins)

# scene set-up
arrows = bpy.data.collections["Spin Arrows"].objects

op.Paramagnetism()
rot.SpinsRotator(op.spins_tensor,"z",0)
for arrow in arrows:
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 10)
    arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0].keyframe_insert(data_path="default_value", frame = 10)

op.Ferromagnetism(np.pi)
rot.SpinsRotator(op.spins_tensor,"z",0)
for arrow in arrows:
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 30)
    arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0].keyframe_insert(data_path="default_value", frame = 30)
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 50)
    arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0].keyframe_insert(data_path="default_value", frame = 50)

op.Ferromagnetism(0)
rot.SpinsRotator(op.spins_tensor,"z",0)
for arrow in arrows:
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 90)
    arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0].keyframe_insert(data_path="default_value", frame = 90)
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 110)
    arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0].keyframe_insert(data_path="default_value", frame = 110)

op.Paramagnetism()
rot.SpinsRotator(op.spins_tensor,"z",0)
for arrow in arrows:
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 150)
    arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0].keyframe_insert(data_path="default_value", frame = 150)