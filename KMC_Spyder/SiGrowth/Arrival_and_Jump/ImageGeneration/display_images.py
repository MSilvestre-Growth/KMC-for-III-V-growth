""" Copy this file to create images of your simulation in path + file name"""

import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from PIL import Image

path = "C:/Users/msilvestre/Documents/GitHub/Images/SiGrowth/steps_4_test/"

possible_types = ['B18','B18i','A19', 'A19i', 'B20', 'B20i', 'A21', 'A21i', 'B22', 'B22i', 'A23', 'A23i', 'B24', 'B24i', 'A25', 'A25i', 'B26', 'B26i', 'A27', 'A27i', 'B28', 'B28i', 'A29', 'A29i', 'B30', 'B30i', 'A31', 'A31i', 'B32', 'B32i', 'A33', 'A33i', 'B34', 'B34i']
#colors = [0, 0.4, 0.2, 0.8, 0.6, 1]
colors = [(0,125,0),(0,125,60),(0,0,125),(0,60,125),(125,0,0),(125,60,0),(0,125,0),(0,125,60),(0,0,250),(0,60,250),(250,0,0),(250,60,0),(0,250,0),(0,250,60),(0,0,125),(0,60,125),(125,0,0),(125,60,0),(0,125,0),(0,125,60)]
colors = np.array(colors, dtype=np.uint8)

types_bis = types

# Growth rate tracking
a=0
ML_s = 0
growth_list = []

A19_list = []
B20_list = []
A21_list = []
B22_list = []
A23_list = []
B24_list = []

for j in range(len(types)):
    a = 0
    A19 = 0
    B20 = 0
    A21 = 0
    B22 = 0
    A23 = 0
    B24 = 0
    for i in range(len(types[0])):
        if types[j][i] == "A19" or types[j][i] == "A19i":
            A19 += 1
        if types[j][i] == "B20" or types[j][i] == "B20i":
            B20 += 1
        if types[j][i] == "A21" or types[j][i] == "A21i":
            A21 += 1    
        if types[j][i] == "B22" or types[j][i] == "B22i":
            B22 += 1     
        if types[j][i] == "A23" or types[j][i] == "A23i":
            A23 += 1     
        if types[j][i] == "B24" or types[j][i] == "B24i":
            B24 += 1    
            
        if types[j][i] != types[0][i]:
            a += int(types[j][i][1:3]) - int(types[0][i][1:3])
    if times[j] == 0:
        ML_s = 0
    else:
        ML_s = (a/10000) * (1/times[j])
            
    growth_list.append(ML_s)
    A19_list.append((A19 + A23) * 100 / 10000)
    B20_list.append((B20 + B24) * 100 / 10000)
    A21_list.append(A21 * 100 / 10000)
    B22_list.append(B22 * 100 / 10000)

plt.plot(times, growth_list)
plt.title("Flux")
plt.figure()
plt.plot(times, A19_list, label="A19")
plt.plot(times, B20_list, label="B20")
plt.plot(times, A21_list, label="A21")
plt.plot(times, B22_list, label="B22")
plt.title("coverage")
plt.legend()
    
# ###################
# #    file name    #
# ###################
# for i in range(len(types)):
#     file_name = "Imtest%d.png" % i
#     KMC_Result_current = types[i]
#     # Conversion of "U" in 1 and "D" in 0 for display purposes
#     for j in range(len(KMC_Result_current)):
#         for k in range(len(possible_types)):
#             if KMC_Result_current[j] == possible_types[k]:
#                 KMC_Result_current[j] = colors[k]
    
#     # Using islice to turn KMC_Result_current (list) in KMC_Result_current_matrix (100x100 matrix)
#     length_to_split = 100 * np.ones(100)
#     KMC_Result_current = iter(KMC_Result_current)
#     KMC_Result_current_matrix = [list(islice(KMC_Result_current, int(elem))) for elem in length_to_split]
#     KMC_Result_current_matrix = np.array(KMC_Result_current_matrix)
    
#     #Image display
#     #plt.figure()
#     #plt.imshow(KMC_Result_current_matrix)
        
#     #Image saving in other directory
#     plt.imsave(path+file_name, KMC_Result_current_matrix)   