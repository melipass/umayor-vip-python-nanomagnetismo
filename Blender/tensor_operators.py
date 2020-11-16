import numpy as np
import random

# I may implement Qiskit's Bloch sphere in order to get non-binary positions

class TensorOperators():
    def __init__(self,spins_array):
        self.spins_array = spins_array
        self.spins_tensor = np.zeros((spins_array[0],spins_array[1],spins_array[2]))
        #print(self.spins_tensor)
        self.Paramagnetism()

    def Ferromagnetism(self,spin_direction):
        for x in range(self.spins_array[0]):
            for y in range(self.spins_array[1]):
                for z in range(self.spins_array[2]):
                    self.spins_tensor[x,y,z] = spin_direction
    
    def Antiferromagnetism(self,spin_direction):
        i = 0
        if spin_direction == 1:
            i = 1
        for z in range(self.spins_array[2]):
            for y in range(self.spins_array[1]):
                for x in range(self.spins_array[0]):
                    self.spins_tensor[x,y,z] = (i%2)
                    i += 1

    def Paramagnetism(self):
        random.seed()
        for x in range(self.spins_array[0]):
            for y in range(self.spins_array[1]):
                for z in range(self.spins_array[2]):
                    self.spins_tensor[x,y,z] = random.choice([0,1])