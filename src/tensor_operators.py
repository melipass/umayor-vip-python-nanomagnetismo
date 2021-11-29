import numpy as np
import random
import os

class TensorOperators():
    """Operators for pre-defined nanomagnetism phenomena.

    All methods within this class are meant to represent a specific
    nanomagnetic configuration and are used to rotate the spins array
    accordingly. The default state of an operator instance is paramagnetism.
    """
    def __init__(self, spins_array):
        self.spins_array = spins_array
        self.spins_tensor = np.zeros((spins_array[0], spins_array[1],
                                      spins_array[2]))
        self.Paramagnetism()

    def Ferromagnetism(self, spin_direction):
        for x in range(self.spins_array[0]):
            for y in range(self.spins_array[1]):
                for z in range(self.spins_array[2]):
                    self.spins_tensor[x, y, z] = spin_direction
        return self.spins_tensor

    def Antiferromagnetism(self, spin_direction):
        i = 0
        for z in range(self.spins_array[2]):
            for y in range(self.spins_array[1]):
                for x in range(self.spins_array[0]):
                    if (i % 2 == 0):
                        self.spins_tensor[x, y, z] = spin_direction
                    else:
                        self.spins_tensor[x, y, z] = spin_direction+np.pi
                    i += 1
        return self.spins_tensor

    def Paramagnetism(self):
        random.seed()
        for x in range(self.spins_array[0]):
            for y in range(self.spins_array[1]):
                for z in range(self.spins_array[2]):
                    self.spins_tensor[x, y, z] = random.uniform(0, 2*np.pi)
        return self.spins_tensor

    def AutomataMatrix(self, matrix):
        row_number = 0
        for row in matrix:
            col_number = 0
            for col in row:
                if col == -1:
                    self.spins_tensor[row_number, col_number, 0] = np.pi
                else:
                    self.spins_tensor[row_number, col_number, 0] = 0
                col_number = col_number + 1
            row_number = row_number + 1
        return self.spins_tensor

    def OperationMatrix(self, spin_direction):
        M = np.matrix(spin_direction)
        vec_1 = np.array([-1, 0, 1])
        vec_2 = np.array([-2, 0, 2])
        vec_3 = np.array([-3, 0, 3])
        for x in range(self.spins_array[0]):
            for y in range(self.spins_array[1]):
                for z in range(self.spins_array[2]):
                    if(vec_1.dot(M)):
                        self.spins_tensor[x, y, z] = spin_direction
                    elif(vec_2.tensor(M)):
                        self.spins_tensor[x, y, z] = spin_direction
                    elif (vec_3.dot(M)):
                        self.spins_tensor[x, y, z] = spin_direction
                    else:
                        self.spins_tensor[x, y, z] = spin_direction
        return self.spins_tensor
