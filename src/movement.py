

import bpy
import mathutils
import numpy as np

arrows = bpy.data.collections["Spin Arrows"].objects

# one blender unit in x-direction
vec = mathutils.Vector((1.0, 0.0, 0.0))
inv = arrows.matrix_world.copy()
inv.invert()
# vec aligned to local axis in Blender 2.8+
# in previous versions: vec_rot = vec * inv
vec_rot = vec @ inv
arrows.location = arrows.location + vec_rot