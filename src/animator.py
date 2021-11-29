import bpy
import rotator

scene = bpy.context.window.scene
bobject = bpy.ops.object
collections = bpy.data.collections
transform = bpy.ops.transform


class Animator():
    def __init__(self, spins):
        self.arrows = collections["Spin Arrows"].objects
        self.rot = rotator.Rotator(spins)
        self.arrows = bpy.data.collections["Spin Arrows"].objects

    def ArrowAnimation(self, objective_state_operator, keyframe,
                       delta=60, delay=0, phase_shift=0, axis="z"):
        d_p_a = "rotation_euler"
        d_p_c = "default_value"
        for arrow in self.arrows:
            arrow.keyframe_insert(data_path=d_p_a, frame=keyframe)
            arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0]\
                .keyframe_insert(data_path=d_p_c, frame=keyframe)
        self.rot.SpinsRotator(objective_state_operator, axis, phase_shift)
        for arrow in self.arrows:
            arrow.keyframe_insert(data_path=d_p_a, frame=keyframe + delta)
            arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0]\
                .keyframe_insert(data_path=d_p_c, frame=keyframe + delta)

    def ClearAnimations(self):
        for arrow in self.arrows:
            arrow.animation_data_clear()
#           arrow.active_material.node_tree.nodes["Principled BSDF"].inputs[0]\
#               .keyframe_delete(data_path="default_value")
