import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


rows = columns = 16 # must be N in 2^N
time = 20 # amount of matrices

# random matrix generation
mat_X = np.random.randint(0, 2, size=(rows, columns))


# Zeros as -1
for f in range(rows):
    for c in range(columns):
      if mat_X[f,c] == 0:
        mat_X[f,c] = -1

# Alternative to using a for loop:
# matriz = np.matrix(np.where(matriz>0,matriz,-1))

mat_Y = np.copy(mat_X)
mat_Z = np.copy(mat_X)

# -1 as red and 1 as black in matplotlib's matrix
cmap = mpl.colors.ListedColormap(['r', 'k'])
bounds = [0., 0.5, 1.]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

for it in range(time):
    for r in range(rows):
        r_plus = r+1
        r_minus = r-1
        sum_mat_X = 0
        for c in range(columns):
            c_plus = c+1
            c_minus = c-1
            if r_plus == rows:
                r_plus = 0
            if r_minus == -1:
                r_minus = rows-1
            if c_plus == columns:
                c_plus = 0
            if c_minus == -1:
                c_minus = columns-1
            sum_mat_X = (mat_X[r_plus, c] + mat_X[r_minus, c]
                         + mat_X[r, c_plus] + mat_X[r, c_minus])
            if sum_mat_X == 0:
                mat_Z[r, c] = -1 * mat_Y[r, c]
    mat_Y=np.copy(mat_X)
    mat_X=np.copy(mat_Z)
    matrix_name = 'matrix-' + str(it) + '.txt'
    np.savetxt('../Blender/out/' + matrix_name, mat_X.astype(int),
               fmt='%i', delimiter=",")
