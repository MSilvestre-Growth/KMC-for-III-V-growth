""" Copy this file to create images of your simulation in path + file name"""

import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from PIL import Image

path = "C:/Users/msilvestre/Documents/GitHub/Images/SiGrowth/steps_4_test/"

possible_types = ['A1', 'A1i', 'B2', 'B2i', 'A3', 'A3i', 'B4', 'B4i', 'A5', 'A5i', 'B6', 'B6i', 'A7', 'A7i', 'B8', 'B8i', 'A9', 'A9i']
#colors = [0, 0.4, 0.2, 0.8, 0.6, 1]
colors = [(0,0,125),(0,60,125),(125,0,0),(125,60,0),(0,125,0),(0,125,60),(0,0,250),(0,60,250),(250,0,0),(250,60,0),(0,250,0),(0,250,60),(0,0,125),(0,60,125),(125,0,0),(125,60,0),(0,125,0),(0,125,60)]
colors = np.array(colors, dtype=np.uint8)

types_bis = types


for i in range(len(types_bis)):
    # #Flux measure not working 
    # Nb_atoms_deposited = 0


    # for l in range(len(types_bis[0])):
    #     toto =  int(types_bis[i][l][1])
    #     tata = int(types_bis[i+1][l][1])
    #     titi = tata - toto
    #     Nb_atoms_deposited += titi

    # print('Nb_atoms_deposited =')
    # print(Nb_atoms_deposited)
    
    ###################
    #    file name    #
    ###################
    file_name = "Imtest%d.png" % i
    KMC_Result_current = types[i]
    # Conversion of "U" in 1 and "D" in 0 for display purposes
    for j in range(len(KMC_Result_current)):
        for k in range(len(possible_types)):
            if KMC_Result_current[j] == possible_types[k]:
                KMC_Result_current[j] = colors[k]
    
    # Using islice to turn KMC_Result_current (list) in KMC_Result_current_matrix (100x100 matrix)
    length_to_split = np.ones(25)
    KMC_Result_current = iter(KMC_Result_current)
    KMC_Result_current_matrix = [list(islice(KMC_Result_current, int(elem))) for elem in length_to_split]
    KMC_Result_current_matrix = np.array(KMC_Result_current_matrix)
    
    #Image display
    #plt.figure()
    #plt.imshow(KMC_Result_current_matrix)
    
    #Image saving in other directory
    plt.imsave(path+file_name, KMC_Result_current_matrix)
