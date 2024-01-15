# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

path = "C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Arrival_test/"

####################
#    Image size    #
####################

X = 80
Y = 30
Z = 10

####################

max_dimension = max([X, Y, Z])

for i in range(len(types)):
    
    file_name = "Imtest%d.png" % i
    KMC_Result_current = types[i]
    
    Voids = np.full((X, Y, Z), False)
    A_Si = np.full((max_dimension, max_dimension, max_dimension), False)
    B_Si = np.full((max_dimension, max_dimension, max_dimension), False)
    A_GaAs = np.full((max_dimension, max_dimension, max_dimension), False)
    B_GaAs = np.full((max_dimension, max_dimension, max_dimension), False)
    A = np.full((max_dimension, max_dimension, max_dimension), False)
    B = np.full((max_dimension, max_dimension, max_dimension), False)
    C = np.full((max_dimension, max_dimension, max_dimension), False)
    D = np.full((max_dimension, max_dimension, max_dimension), False)
    
    # Interface states
    Vt = np.full((max_dimension, max_dimension, max_dimension), False)
    
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "A_Si":
                    A_Si[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "B_Si":
                    B_Si[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "A_GaAs":
                    A_GaAs[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "B_GaAs":
                    B_GaAs[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "A":
                    A[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "B":
                    B[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "C":
                    C[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "D":
                    D[x][y][z] = True
                
                # Interface states
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "Vt":
                    Vt[x][y][z] = True                  
    
    #combine the objects into a single boolean array
    voxelarray = A_Si | B_Si | A_GaAs | B_GaAs | A | B | C | D#| Vt
    
    colors = np.empty(voxelarray.shape, dtype=object)
    #colors[void] = '#FF000000' # == transparent
    colors[A_Si] = 'grey'
    colors[B_Si] = 'grey'
    colors[A_GaAs] = 'blue'
    colors[B_GaAs] = 'yellow'
    colors[A] = 'red'
    colors[B] = 'orange'
    colors[C] = 'purple'
    colors[D] = 'pink'
    
    # # Interface states
    # colors[Vt] = 'green'
    
    ax = plt.axes(projection='3d')
    
    # turn off/on axis
    plt.axis('off')
    #settings
    # X-axis : left 7.8908618514956235
    # X-axis : right 33.60440199006097
    # Y-axis : bottom -6.302167259329746
    # Y-axis : top 19.411372879235586
    plt.xlim((10.268365867838938,35.98190600640428))
    plt.ylim((-12.04950983931609,13.66403029924924))
    
    ax.voxels(voxelarray, facecolors=colors, edgecolor='#FF000000')
    plt.savefig(path+file_name) 
    plt.close()