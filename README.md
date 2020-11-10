![Universidad Mayor and Vertically Integrated Projects logo](umayor-vip-header.png)

# umayor-vip-python-nanomagnetismo

## About this repo
This repository contains Python code I wrote during Universidad Mayor's Vertically Integrated Project **Python animations for applications in nanomagnetism**. [Read more](https://cib.umayor.cl/en/news/vip-projects-the-tool-that-fosters-the-link-between-undergraduate-and-research-carried-out-in-the-u-mayor).
Some comments within the code are written in Spanish.

To make the code work within a Blender project, you have to store the Python files in the same folder as the .blend file and add the following code in the project's Text Editor under the Scripting tab.
```python
import bpy
import os

# Replace [FILENAME] with the file you want to run
filename = os.path.join(os.path.dirname(bpy.data.filepath), "[FILENAME].py") 
exec(compile(open(filename).read(), filename, 'exec'))
```

## Acerca de este repo
El código que se encuentra dentro de este repositorio corresponde al código que realicé durante el proyecto VIP de **Animaciones en Python para aplicaciones en nanomagnetismo** de la Universidad Mayor. [Leer más](https://cib.umayor.cl/news/proyectos-vip-la-herramienta-que-fomenta-la-vinculaci%C3%B3n-entre-el-pregrado-y-la-investigaci%C3%B3n-que-se-realiza-en-la-u-mayor).

Para hacer que el código funcione dentro de un proyecto de Blender, debes almacenar los archivos en la misma carpeta que el archivo .blend y agregar el siguiente texto en la ventana del proyecto llamada Text Editor, de la pestaña Scripting.

```python
import bpy
import os

# Cambia [FILENAME] por el nombre del archivo que quieres correr
filename = os.path.join(os.path.dirname(bpy.data.filepath), "[FILENAME].py") 
exec(compile(open(filename).read(), filename, 'exec'))
```
