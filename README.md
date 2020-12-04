![Universidad Mayor and Vertically Integrated Projects logo](umayor-vip-header.png)

# umayor-vip-python-nanomagnetismo
<p align="center">
<img src="Blender/paramagnetism.png" width="70%">
</p>

## About this repo
This repository contains Python code I wrote during Universidad Mayor's Vertically Integrated Project **Python animations for applications in nanomagnetism**. [Read more](https://cib.umayor.cl/en/news/vip-projects-the-tool-that-fosters-the-link-between-undergraduate-and-research-carried-out-in-the-u-mayor).
Keep in mind that this is in an early development stage.

To make the code work within a Blender project, you have to store the Python files in the same folder as the .blend file and add the following code in the project's Text Editor under the Scripting tab. It loads the demo.py file.
```python
import bpy
import os
import sys

sys.path.append(bpy.path.abspath("//"))
filename = os.path.join(os.path.dirname(bpy.data.filepath), "demo.py") 
exec(compile(open(filename).read(), filename, 'exec'))
```

## Acerca de este repo
El código que se encuentra dentro de este repositorio corresponde al código que realicé durante el proyecto VIP de **Animaciones en Python para aplicaciones en nanomagnetismo** de la Universidad Mayor. [Leer más](https://cib.umayor.cl/news/proyectos-vip-la-herramienta-que-fomenta-la-vinculaci%C3%B3n-entre-el-pregrado-y-la-investigaci%C3%B3n-que-se-realiza-en-la-u-mayor). Importante considerar que el proyecto está en una etapa de desarrollo inicial.

Para hacer que el código funcione dentro de un proyecto de Blender, debes almacenar los archivos en la misma carpeta que el archivo .blend y agregar el siguiente texto en la ventana del proyecto llamada Text Editor, de la pestaña Scripting. Carga el archivo demo.py.

```python
import bpy
import os
import sys

sys.path.append(bpy.path.abspath("//"))
filename = os.path.join(os.path.dirname(bpy.data.filepath), "demo.py") 
exec(compile(open(filename).read(), filename, 'exec'))
```
