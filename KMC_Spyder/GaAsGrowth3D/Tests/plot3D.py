# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

####################
#    Image size    #
####################

X = 5
Y = 5
Z = 5

####################
 
ax = plt.axes(projection='3d')

void = np.full((X, Y, Z), False)
Si = np.full((X, Y, Z), False)

types = ["V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V",
              "V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V",
              "V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V",
              "V","V","V","V","V","V","V","Si","V","V","V","V","V","V","V","V","V","V","V",
              "V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V",
              "V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V","V",
              "V","V","V","V","V","V","V","V","V","V","V"]

for x in range(X):
    for y in range(Y):
        for z in range(Z):
            if types[(Y*Z) * x + (Z) * y + (1) * z] == "Si":
                Si[x][y][z] = True

#combine the objects into a single boolean array
voxelarray = Si          

colors = np.empty(voxelarray.shape, dtype=object)
#colors[void] = '#FF000000' # == transparent
colors[Si] = 'red'

plt.figure()
ax.voxels(voxelarray, facecolors=colors, edgecolor='#FF000000')
