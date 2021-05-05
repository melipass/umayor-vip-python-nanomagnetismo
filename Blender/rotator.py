import bpy, bmesh, math
import numpy as np

# shorten text to work with
scene = bpy.context.window.scene
bobject = bpy.ops.object
collections = bpy.data.collections
transform = bpy.ops.transform

class Rotator():
    def __init__(self,spins):
        self.spins_array = spins
        bobject.select_all(action="DESELECT")
        self.value_list = []
    
    def CollectionRotator(self,tensor,axis,phase_shift):
        for x in np.nditer(tensor, order="C"):
            self.value_list.append(x)
            print(x)
        i = 0
        for o in collections["Spin Arrows"].objects:
            #o.rotation_euler = self.value_list[i]+phase_shift
            i += 1
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