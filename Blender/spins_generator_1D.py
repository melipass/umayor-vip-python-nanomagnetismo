import bpy, bmesh, random

number_of_spins = 10
electron_radius = 5
distance_between_spins = 2

# Método para poblar el espacio de trabajo de Blender con objetos que representan spins, posicionados en 1D.
def CreateSpinsArray():
    # Borro objetos ya existentes (en caso de cargar este script en nuevo entorno)
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    
    # Importo el OBJ flecha y le asigno nombre
   # bpy.ops.import_scene.obj(filepath=r"D:\Universidad\S08 - 2020\VIP\Blender\arrow.obj")
   # bpy.context.selected_objects[0].name = 'Arrow'
   # bpy.context.selected_objects[0].data.name = 'Arrow'
   # bpy.context.selected_objects[0].modifier_add(type='ARRAY')
   
   # Creo un array de esferas que representará el electron.
   # Al ser un array, cada esfera compartirá parámetros
    bpy.ops.mesh.primitive_uv_sphere_add(scale=(electron_radius,electron_radius,electron_radius))
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.ops.object.shade_smooth()
    bpy.data.objects["Sphere"].modifiers["Array"].count = number_of_spins
    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = distance_between_spins
    
    # Creo una colección de cilindros que representarán la flecha del spin.
	# Al ser instanciados de a uno  y movidos a una colección, cada cilindro tendrá sus parámetros propios.
    bpy.ops.mesh.primitive_cylinder_add(scale=(electron_radius*.1, electron_radius*.1, electron_radius*1.5))
    bpy.ops.object.move_to_collection(collection_index=2)
    for i in range(number_of_spins-1):
        bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(distance_between_spins * electron_radius,0,0)})
        bpy.ops.object.shade_smooth()
        bpy.ops.object.move_to_collection(collection_index=2)

CreateSpinsArray()