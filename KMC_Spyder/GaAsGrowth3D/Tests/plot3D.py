# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

path = "C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Arrival_test/"

####################
#    Image size    #
####################

X = 40
Y = 10
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
    
    # Interface states
    Ai_Si = np.full((max_dimension, max_dimension, max_dimension), False)
    Bi_Si = np.full((max_dimension, max_dimension, max_dimension), False)
    Ai_GaAs = np.full((max_dimension, max_dimension, max_dimension), False)
    Bi_GaAs = np.full((max_dimension, max_dimension, max_dimension), False)
    
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
                
                # Interface states
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "Ai_Si":
                    Ai_Si[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "Bi_Si":
                    Bi_Si[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "Ai_GaAs":
                    Ai_GaAs[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "Bi_GaAs":
                    Bi_GaAs[x][y][z] = True
    
    #combine the objects into a single boolean array
    voxelarray = A_Si | B_Si | A_GaAs | B_GaAs | Ai_Si | Bi_Si | Ai_GaAs | Bi_GaAs
    
    colors = np.empty(voxelarray.shape, dtype=object)
    #colors[void] = '#FF000000' # == transparent
    colors[A_Si] = 'grey'
    colors[B_Si] = 'grey'
    colors[A_GaAs] = 'blue'
    colors[B_GaAs] = 'yellow'
    
    # Interface states
    colors[Ai_Si] = 'k'
    colors[Bi_Si] = 'k'
    colors[Ai_GaAs] = 'purple'
    colors[Bi_GaAs] = 'orange'
    
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