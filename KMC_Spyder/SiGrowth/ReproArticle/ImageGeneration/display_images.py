""" Copy this file to create images of your simulation in path + file name"""

import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from PIL import Image

path = "C:/Users/msilvestre/Documents/GitHub/Images/SiGrowth/steps_4_test/"

possible_types = ['A1','B2', 'A3', 'B4', 'A5', 'B6']
#colors = [[0,0,125],[150,0,0],[0,0,175],[200,0,0],[0,0,225],[250,0,0]]

for i in range(len(types)):
    ###################
    #    file name    #
    ###################
    file_name = "Imtest%d.png" % i
    KMC_Result_current = types[i]
    # Conversion of "U" in 1 and "D" in 0 for display purposes
    for j in range(len(KMC_Result_current)):
        for k in range(len(possible_types)):
            if KMC_Result_current[j] == possible_types[k]:
                KMC_Result_current[j] = k/len(possible_types)
    
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
