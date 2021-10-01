import numpy as np

class Automata():
    def __init__(self, n = 4, times = 3):
        self.filas = self.columnas = n
        self.times = times
        self.matrices = []

    def GenerateAutomata(self):
        filas = self.filas
        columnas = self.columnas
        times = self.times
        mat_X = np.random.randint(0,2,size=(self.filas, self.columnas))

        for f in range(filas):
            for c in range(columnas):
                if mat_X[f,c] == 0:
                    mat_X[f,c] = -1
        mat_Y = mat_X
        mat_Z = mat_X
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
                        #print(mat_Y)
                        #print()
            
            #print()
            #print(mat_Y)
            self.matrices.append(mat_Y)
            mat_Y = mat_X
            mat_X = mat_Z
        return self.matrices

automata = Automata(4,5)
automata.GenerateAutomata()
#print(automata.GenerateAutomata())
for i in automata.GenerateAutomata():
    print(i)