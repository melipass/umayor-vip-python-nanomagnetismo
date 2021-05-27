import bpy, bmesh, math
import numpy as np

scene = bpy.context.window.scene
bobject = bpy.ops.object
collections = bpy.data.collections
transform = bpy.ops.transform

class Rotator():
    """Takes care of rotating spin arrows.
    
    This class manages everything related to the spin arrow angles. Blender has the
    bpy.ops.transform.rotate() function and the bpy.data.collections.rotation_euler
    parameter in 3D objects, and their usage should be made clear in future versions.
    Both work with radians instead of angles, so numpy is used to avoid accumulating
    lag when rotating by pi times x.

    Attributes
    ----------
    number_of_spins : [int]
        the spin array dimensions, e.g. [3,5,2]"""

    def __init__(self,number_of_spins):
        self.spins_array = number_of_spins
        bobject.select_all(action="DESELECT")
        self.value_list = []
    
    def SpinsRotator(self,operator,axis,phase_shift):
        """Rotates a collection of spin arrow objects according to the values inside
        the given operator array."""
        axis = axis.lower()
        for x in np.nditer(operator, order="C"): # np.nditer is numpy's n-dimension iterator
            self.value_list.append(x)

        i = 0
        if axis == "x":    
            for o in collections["Spin Arrows"].objects:
                o.rotation_euler = (self.value_list[i]+phase_shift,0.0,0.0)
                self.SpinsColor(o, 0, i)
                i += 1
        elif axis == "y":
            for o in collections["Spin Arrows"].objects:
                o.rotation_euler = (0.0,self.value_list[i]+phase_shift,0.0)
                self.SpinsColor(o, 1, i)
                i += 1
        else:
            for o in collections["Spin Arrows"].objects:
                o.rotation_euler = (0.0,0.0,self.value_list[i]+phase_shift)
                self.SpinsColor(o, 2, i)
                i += 1

    def SpinsColor(self, o, axis, i):
        if o.rotation_euler[axis] > np.pi/2 and o.rotation_euler[axis] < 3*np.pi/2:
            red = 1
            blue = 0
            green = 0
        else:
            blue = 1
            red = 0
            green = 0
        self.MaterialGenerator(o,"Spin color " + str(i),red,green,blue)

    def MaterialGenerator(self, obj, material_name, r, g, b):
        material = bpy.data.materials.get(material_name)
        if material is None:
            material = bpy.data.materials.new(material_name)
        material.use_nodes = True
        principled_bsdf = material.node_tree.nodes['Principled BSDF']
        principled_bsdf.inputs[0].default_value = (r, g, b, 1)
        obj.active_material = material