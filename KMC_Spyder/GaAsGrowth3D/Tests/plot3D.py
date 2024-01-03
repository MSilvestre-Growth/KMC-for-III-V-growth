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

types = ["V","V","V","V","V","V","V","V","V","V","V","V","V","V","Si","V","V","V","V",
              "V","V","V","V","V","V","V","V"]

for x in range(3):
    for y in range(3):
        for z in range(3):
            if types[9*x + 3*y + 1*z] == "V":
                void[x][y][z] = True
            else:
                Si[x][y][z] = True
                
#combine the objects into a single boolean array
voxelarray = Si          

colors = np.empty(voxelarray.shape, dtype=object)
#colors[void] = '#FF000000' # == transparent
colors[Si] = 'red'

ax.voxels(voxelarray, facecolors=colors, edgecolor='#FF000000')

plt.show()