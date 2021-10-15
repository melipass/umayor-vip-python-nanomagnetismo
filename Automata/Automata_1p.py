#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

filas = columnas = 4

#Generacion de matriz aleatoria. >=0 <2
mat_X = np.random.randint(0,2,size=(filas, columnas))

#Cambio ceros a "-1"
for f in range(filas):
    for c in range(columnas):
      if mat_X[f,c] == 0:
        mat_X[f,c] = -1

mat_Y = mat_X
mat_Z = mat_X

#%%Repeticiones
times = 3

#%%Definicion de colores
cmap = mpl.colors.ListedColormap(['r', 'k'])
bounds = [0., 0.5, 1.]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

matrices = []

#%%Bordes, aplicación de la Regla
for iT in range(times):
    for f in range(filas):
        f_mas = f+1
        f_menos = f-1
        sum_mat_X = 0
    
        for c in range(columnas):
            c_mas = c+1
            c_menos = c-1

            if f_mas == filas:
                f_mas = 0
                
            if f_menos == -1:
                f_menos = filas-1
                
            if c_mas == columnas:
                c_mas = 0

            if c_menos == -1:
                c_menos = columnas-1

            sum_mat_X = mat_X[f_mas,c]+mat_X[f_menos,c]+mat_X[f,c_mas]+mat_X[f,c_menos]
            if sum_mat_X == 0:
                mat_Z[f,c] = -1 * mat_Y[f,c]
                print(mat_Z)
    print("==============A================")
    print(mat_Y)
    print("==")
    print(mat_X)
    print("==")
    print(mat_Z)
    
    mat_Y = mat_X
    mat_X = mat_Z
    print("==============B================")
    print(mat_Y)
    print("==")
    print(mat_X)
    print("==")
    print(mat_Z)
    #%%MOSTRAR LA EVOLUCION DE LA MATRIX mat_Y.
    plt.imshow(mat_Y, interpolation='none',cmap=cmap, norm=norm)

    #Se grafican las Matrices
    plt.show()

for matriz in matrices:
    print(matriz)


###Animacion del automata 

automaton_size = 100
automata1 = Automata(automaton_size)
nb_frames = 100

img = Image.new('RGB', (automaton_size, nb_frames), 'white')
draw = ImageDraw.Draw(img)
fig, ax = plt.subplots(dpi=50, figsize=(5, 5))
####im = ax.imshow(img)###
plt.axis('off')

def animate(i, automaton, draw, img):
    space_img = Image.fromarray(automata1.space.reshape(1, automaton_size)*255)
    img.paste(space_img, (0, i))####mask=space_img
    ax.imshow(img)
    automaton.update(rule_x)

ani = animation.FuncAnimation(fig, animate, frames=nb_frames, interval=1, 
                              fargs=[automata1, draw, img])
