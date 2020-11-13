import bpy, bmesh, random
# shorten text to work with
scene = bpy.context.window.scene
bobject = bpy.ops.object
collections = bpy.data.collections

class Generator():
    def __init__(self,number_of_spins,electron_radius,distance_between_spins):
        self.spins = number_of_spins
        self.er = electron_radius
        self.dbs = distance_between_spins
        # self.arrow_path = bpy.path.abspath("//arrow.obj") # file location relative to the .blend project folder

    def ClearScene(self):
        bobject.select_all(action="SELECT")
        bobject.delete()
        for c in scene.collection.children:
            scene.collection.children.unlink(c)
        for c in bpy.data.collections:
            if not c.users:
                bpy.data.collections.remove(c)

    def ObjectDuplicatorX(self,col_name):
        # keys() method returns an array with the names of all collections in the scene
        col_index = collections.keys().index(col_name)
        bobject.move_to_collection(collection_index=col_index)
        for i in range(self.spins[0]-1):
            i=i
            bobject.duplicate_move(TRANSFORM_OT_translate={"value":(self.dbs * self.er,0,0)})
            bobject.move_to_collection(collection_index=col_index)

    def ObjectDuplicatorY(self, col_name):
        bobject.select_all(action="DESELECT")
        for o in collections[col_name].objects:
            o.select_set(True)
        col_index = collections.keys().index(col_name)
        for i in range(self.spins[1]-1):
            i=i
            bobject.duplicate_move(TRANSFORM_OT_translate={"value":(0, self.dbs * self.er,0)})
            bobject.move_to_collection(collection_index=col_index)

    def ObjectDuplicatorZ(self, col_name):
        bobject.select_all(action="DESELECT")
        for o in collections[col_name].objects:
            o.select_set(True)
        col_index = collections.keys().index(col_name)
        for i in range(self.spins[2]-1):
            i=i
            bobject.duplicate_move(TRANSFORM_OT_translate={"value":(0, 0, self.dbs * self.er)})
            bobject.move_to_collection(collection_index=col_index)

    def Create1DSpinsArray(self):
        # Electron sphere object(s) generation
        current_collection = collections.new(name="Electrons") # creating a collection
        scene.collection.children.link(current_collection) # adding it to the scene
        bpy.ops.mesh.primitive_uv_sphere_add(scale=(self.er,self.er,self.er)) # creating sphere
        bobject.shade_smooth()
        self.ObjectDuplicatorX(current_collection.name)
        
        # Spin arrow object(s) generation
        current_collection = collections.new(name="Spin Arrows")
        scene.collection.children.link(current_collection)
        bpy.ops.import_scene.obj(filepath=bpy.path.abspath("//arrow.obj"))
        bpy.ops.transform.resize(value=(1.0, 1.0, self.er/3))
        bobject.shade_smooth()
        self.ObjectDuplicatorX("Spin Arrows")

    def Create2DSpinsArray(self):
        self.Create1DSpinsArray()
        self.ObjectDuplicatorY("Electrons")
        self.ObjectDuplicatorY("Spin Arrows")

    def Create3DSpinsArray(self):
        self.Create2DSpinsArray()
        self.ObjectDuplicatorZ("Electrons")
        self.ObjectDuplicatorZ("Spin Arrows")
        