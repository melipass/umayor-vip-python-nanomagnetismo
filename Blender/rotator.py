import bpy, bmesh, math
import numpy as np

# shorten text to work with
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
        the spin array dimensions, e.g. [3,5,2]

    TODO: Color should change dynamically when the arrow changes direction."""

    def __init__(self,number_of_spins):
        self.spins_array = number_of_spins
        bobject.select_all(action="DESELECT")
        self.value_list = []
    
    def CollectionRotator(self,operator,axis,phase_shift):
        """Rotates spin arrows according to the values inside the operator array."""
        axis = axis.lower()
        for x in np.nditer(operator, order="C"): # np.nditer = numpy's n-dimension iterator
            self.value_list.append(x)
            print(x)
        i = 0
        if axis == "x":    
            for o in collections["Spin Arrows"].objects:
                o.rotation_euler = (self.value_list[i],0.0,0.0)#+phase_shift
                i += 1
        elif axis == "y":
            for o in collections["Spin Arrows"].objects:
                o.rotation_euler = (0.0,self.value_list[i],0.0)#+phase_shift
                i += 1
        else:
            for o in collections["Spin Arrows"].objects:
                o.rotation_euler = (0.0,0.0,self.value_list[i])#+phase_shift
                i += 1

#        for x in np.nditer(operator, order="C"):
#            self.value_list.append(x)
#            print(x)
#        i = 0
##        for o in collections["Spin Arrows"].objects:
##            o.rotation_euler = self.value_list[i]+phase_shift
##            i += 1
#            bobject.select_all(action="DESELECT")
#            #print(self.value_list[i])
#            o.select_set(True)
#            transform.rotate(value=self.value_list[i],orient_axis=axis)
#            if np.sin(self.value_list[i] + phase_shift) > 0:
#                red = np.sin(self.value_list[i] + phase_shift)+0.01
#                blue = 0
#                green = 0#np.cos(np.abs((self.value_list[i] + phase_shift)+np.pi/2))*0.1
#            else:
#                blue = -np.sin(self.value_list[i] + phase_shift)+0.01
#                red = 0
#                green = 0#np.cos(np.abs((self.value_list[i] + phase_shift)+np.pi/2))*0.1
#            self.SpinRotationMaterial(o,"Spin color " + str(i),red,green,blue)
#            bpy.ops.object.select_all(action="DESELECT")
#            i += 1
             
    def SpinRotationMaterial(self, obj, material_name, r, g, b):
        material = bpy.data.materials.get(material_name)
        if material is None:
            material = bpy.data.materials.new(material_name)
        material.use_nodes = True
        principled_bsdf = material.node_tree.nodes['Principled BSDF']
        if principled_bsdf is not None:
            principled_bsdf.inputs[0].default_value = (r, g, b, 1)  
        obj.active_material = material

    def CollectionRotatorY(self):
        pass
    def CollectionRotatorZ(self):
        pass