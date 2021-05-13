import bpy, bmesh, math
import numpy as np

scene = bpy.context.window.scene
bobject = bpy.ops.object
collections = bpy.data.collections
transform = bpy.ops.transform

class Animator():
    """Ideally, this should be the class that manages the keyframes. WIP"""

    def __init__(self):
        self.arrows = collections["Spin Arrows"].objects

    def SimpleAnimation(first_state, second_state, delta_time, delay):
        rotator()