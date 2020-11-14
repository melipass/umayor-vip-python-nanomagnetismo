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
    
    def CollectionRotatorX(self,tensor):
        for x in np.nditer(tensor, order="C"):
            self.value_list.append(x)
            print(x)
        i = 0
        for o in collections["Spin Arrows"].objects:
            bobject.select_all(action="DESELECT")
            print(self.value_list[i])
            if self.value_list[i] == 1.0:
                o.select_set(True)
                transform.rotate(value=-3.14, orient_axis='X')
            if self.value_list[i] == 0.0:
                o.select_set(True)
                transform.rotate(value=2*3.14, orient_axis='X')
            i += 1
             

    def CollectionRotatorY(self):
        pass
    def CollectionRotatorZ(self):
        pass