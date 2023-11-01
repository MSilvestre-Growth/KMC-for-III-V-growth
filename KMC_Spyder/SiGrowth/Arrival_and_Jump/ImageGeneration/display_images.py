""" Copy this file to create images of your simulation in path + file name"""

import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from PIL import Image

path = "C:/Users/msilvestre/Documents/GitHub/Images/SiGrowth/steps_4_test/"

possible_types = ['A01', 'A01i', 'B02', 'B02i', 'A03', 'A03i', 'B04', 'B04i', 'A05', 'A05i', 'B06', 'B06i', 'A07', 'A07i', 'B08', 'B08i', 'A09', 'A09i', 'B10', 'B10i', 'A11', 'A11i', 'B12', 'B12i', 'A13', 'A13i', 'B14', 'B14i', 'A15', 'A15i', 'B16', 'B16i', 'A17', 'A17i', 'B18', 'B18i', 'A19', 'A19i', 'B20', 'B20i', 'A21', 'A21i', 'B22', 'B22i', 'A23', 'A23i', 'B24', 'B24i']
#colors = [0, 0.4, 0.2, 0.8, 0.6, 1]
colors = [(0,0,125),(0,60,125),(125,0,0),(125,60,0),(0,125,0),(0,125,60),(0,0,250),(0,60,250),(250,0,0),(250,60,0),(0,250,0),(0,250,60),(0,0,125),(0,60,125),(125,0,0),(125,60,0),(0,125,0),(0,125,60)]
colors = np.array(colors, dtype=np.uint8)

types_bis = types

# Growth rate tracking
a=0
ML_s = 0
growth_list = []

for j in range(len(types)):
    a = 0
    for i in range(len(types[0])):
        if types[j][i] != types[0][i]:
            a += int(types[j][i][1:3]) - int(types[0][i][1:3])
            ML_s = (a/10000) * (1/times[j])
    growth_list.append(ML_s)

plt.plot(times, growth_list)


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
    length_to_split = 100 * np.ones(100)
    KMC_Result_current = iter(KMC_Result_current)
    KMC_Result_current_matrix = [list(islice(KMC_Result_current, int(elem))) for elem in length_to_split]
    KMC_Result_current_matrix = np.array(KMC_Result_current_matrix)
    
    #Image display
    #plt.figure()
    #plt.imshow(KMC_Result_current_matrix)
    
    #Image saving in other directory
    plt.imsave(path+file_name, KMC_Result_current_matrix)
    
    