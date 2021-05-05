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
rot.CollectionRotator(op.spins_tensor,"X",np.pi/2)
for arrow in arrows:
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 10)
    color_node = arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0]
    color_node.default_value = (0,1,0,1)
    color_node.keyframe_insert(data_path="default_value", frame = 10)
op.Ferromagnetism(np.pi)
rot.CollectionRotator(op.spins_tensor,"X",np.pi/2)
for arrow in arrows:
    arrow.keyframe_insert(data_path = "rotation_euler", frame = 30)
    color_node = arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0]
    color_node.default_value = (1,0,0,1)
    color_node.keyframe_insert(data_path="default_value", frame = 30)

#for arrow in arrows:
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 10)
#op.Ferromagnetism(0)
#for arrow in arrows:
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 20)
#op.Ferromagnetism(np.pi)
#for arrow in arrows:
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 40)
#op.Ferromagnetism(0)
#for arrow in arrows:
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 60)

#delay = 0
#for arrow in arrows:
#    rad = arrow.rotation_euler
#    rad.x = rad.x + np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 1 + delay)
#    rad.x = rad.x - np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 50 + delay)
#    rad.x = rad.x + np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 70 + delay)
#    rad.x = rad.x + np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 80 + delay)
#    delay = delay + 0

#rot.CollectionRotator(op.spins_tensor,"X",np.pi/2)
#rot.CollectionRotator(op.spins_tensor,"X",np.pi/2)
#rot.CollectionRotator(op.spins_tensor,"Y",np.pi/2)

#delay = 90
#for arrow in arrows:
#    rad = arrow.rotation_euler
#    rad.y = rad.y + np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 1 + delay)
#    rad.y = rad.y - np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 50 + delay)
#    rad.y = rad.y + np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 70 + delay)
#    rad.y = rad.y + np.pi
#    arrow.keyframe_insert(data_path = "rotation_euler", frame = 80 + delay)
#    delay = delay + 0