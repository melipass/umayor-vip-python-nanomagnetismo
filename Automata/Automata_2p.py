import numpy as np

################estas son las librerias para hacer graficas

import matplotlib.pyplot as plt

import matplotlib as mpl

##############################
### tamaño de la matrix
filas = columnas = 4
### Tiempo de iteracion o cantidad de matrices  
time = 6

#Generacion de matriz aleatoria. >=0 <2

mat_X = np.random.randint(0,2,size=(filas, columnas))


#Cambio ceros a "-1"

for f in range(filas):

    for c in range(columnas):

  # print(f,c, matrix[f,c])

     

      if mat_X[f,c] == 0:

        mat_X[f,c] = -1


#truco, alternative a for

# matriz = np.matrix(np.where(matriz>0,matriz,-1))

mat_Y = np.copy(mat_X)

mat_Z = np.copy(mat_X)


##### AQUI SE DEFINE SOLO DOS COLORES PARA QUE -1 Y 1 TOME ROJO O NEGRO

cmap = mpl.colors.ListedColormap(['r', 'k'])

bounds = [0., 0.5, 1.]

norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

## ESTA ULTIMA ES PARA DEFINIR SOLO LOS BORDES.

#############################

for it in range(time):

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

            # print(f_mas,f_menos,c_mas,c_menos)

            sum_mat_X = mat_X[f_mas,c]+mat_X[f_menos,c]+mat_X[f,c_mas]+mat_X[f,c_menos]

            #print(sum_mat_X)
           
            if sum_mat_X == 0:

                mat_Z[f,c] = -1 * mat_Y[f,c]

    #print("mat_X")
    #print(mat_X);
    #print("mat_Y")
    #print(mat_Y);
    mat_Y=np.copy(mat_X)                        
    mat_X=np.copy(mat_Z)
    nameMatrix='matrix-'+str(it)+'.txt'
    np.savetxt('../Blender/out/'+nameMatrix, mat_X.astype(int), fmt='%i', delimiter=",")







#################################################
