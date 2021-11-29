import bpy
import numpy as np

collections = bpy.data.collections
scene = bpy.context.window.scene
bobject = bpy.ops.object


class Stage():
    def __init__(self):
        self.AddPlane()
        self.PlaneMaterial()
        self.AddSun()
        self.AddCamera()

    def AddPlane(self):
        context = bpy.context
        if context.object:
            bobject.mode_set()
        scene.collection.children.link(collections.new(name='Plane'))
        bpy.ops.mesh.primitive_plane_add(size=1000, location=(0, 0, -20))
        bobject.move_to_collection(collection_index=collections
                                   .keys().index('Plane')+1)
        collections['Plane'].objects[0].select_set(True)
        ob = context.object
        me = ob.data
        me.polygons.foreach_set("select", (False,) * len(me.polygons))
        me.edges.foreach_set("select", (False,) * len(me.edges))
        me.vertices.foreach_set("select",
                                np.array([1, 1, 1, 1], dtype=np.bool))
        bobject.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":
                                         (0, 0, 1000)})
        bobject.mode_set(mode='OBJECT')
        me.vertices.foreach_set("select",
                                np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                                         dtype=np.bool))
        bobject.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='VERT')
        bevel_offsets = [90, 35, 20, 10]
        for offset in bevel_offsets:
            bpy.ops.mesh.bevel(offset=offset, offset_pct=0, affect='EDGES')
        bobject.mode_set(mode='OBJECT')

    def PlaneMaterial(self):
        material = bpy.data.materials.get("Background material")
        if material is None:
            material = bpy.data.materials.new("Background material")
        material.use_nodes = True
        bpy.data.materials["Background material"] \
            .node_tree.nodes["Principled BSDF"].inputs[0]. \
            default_value = (1, 1, 1, 1)
        material.use_nodes = True
        collections['Plane'].objects[0].active_material = material

    def AddSun(self):
        context = bpy.context
        if context.object:
            bobject.mode_set()
        scene.collection.children.link(collections.new(name='Light'))
        bpy.ops.object.light_add(type='SUN',
                                 align='WORLD',
                                 location=(50, -100, 70),
                                 rotation=(0.3, 0.1, 0.2))
        bobject.move_to_collection(collection_index=collections
                                   .keys().index('Light')+2)
        collections['Light'].objects[0].select_set(True)
        bpy.context.object.data.energy = 30
        bpy.context.object.data.use_shadow = False
        bpy.context.object.data.angle = 1.18553

    def AddCamera(self):
        context = bpy.context
        if context.object:
            bobject.mode_set()
        scene.collection.children.link(collections.new(name='Camera'))
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW',
                                  #location=(38, 35, 215),
                                  location=(100, 100, 600),
                                  rotation=(0, 0, 0),
                                  scale=(1, 1, 1))
        bobject.move_to_collection(collection_index=collections
                                   .keys().index('Camera')+5)
        collections['Camera'].objects[0].select_set(True)
