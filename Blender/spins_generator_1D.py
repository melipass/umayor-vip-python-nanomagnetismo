import bpy, bmesh, random

"""
So far, by writing this code, I have seen the following hierarchy:
    context -> window -> scene -> collection -> objects -> meshes
"""

# shorten text to work with
scene = bpy.context.window.scene
object = bpy.ops.object
collections = bpy.data.collections

# variables
spins = [5,0,0] # number of spins
er = 5 # electron radius
dbs = 2 # distance between spins
arrow_path = bpy.path.abspath("//arrow.obj") # file location relative to the .blend project folder

def ClearScene():
    object.select_all(action="SELECT")
    object.delete()
    for c in scene.collection.children:
        scene.collection.children.unlink(c)
    for c in bpy.data.collections:
        if not c.users:
            bpy.data.collections.remove(c)

def ObjectDuplicatorX(col_name):
    # keys() method returns an array with the names of all collections in the scene
    col_index = collections.keys().index(col_name)
    object.move_to_collection(collection_index=col_index)
    for i in range(spins[0]-1):
        object.duplicate_move(TRANSFORM_OT_translate={"value":(dbs * er,0,0)})
        object.move_to_collection(collection_index=col_index)

def Create1DSpinsArray():
    # Electron sphere object(s) generation
    current_collection = collections.new(name="Electrons") # creating a collection
    scene.collection.children.link(current_collection) # adding it to the scene
    bpy.ops.mesh.primitive_uv_sphere_add(scale=(er,er,er)) # creating sphere
    object.shade_smooth()
    ObjectDuplicatorX(current_collection.name)
    
    # Spin arrow object(s) generation
    current_collection = collections.new(name="Spin Arrows")
    scene.collection.children.link(current_collection)
    bpy.ops.import_scene.obj(filepath=arrow_path)
    bpy.ops.transform.resize(value=(1.0, 1.0, er/3))
    object.shade_smooth()
    ObjectDuplicatorX("Spin Arrows")

ClearScene()
Create1DSpinsArray()

# Yet to code:
#def ObjectDuplicatorY(collection_name):
#    for o in collections[collection_name].objects:
#        o.select_set(True)
#    
#def Create2DSpinsArray():
#    Create1DSpinsArray()
#    ObjectDuplicatorY("Electrons")
#    ObjectDuplicatorY("Spin Arrows")