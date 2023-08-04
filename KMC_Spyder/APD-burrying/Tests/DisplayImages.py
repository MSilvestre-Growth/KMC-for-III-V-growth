# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:36:48 2023

@author: msilvestre
"""

import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from PIL import Image

CONFIG_MATRIX_SIDE_SIZE = 30

# types = ['A1']*200
# for i in range(200) :
#     types.append('B1')

types = ['A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','A1','A1','A1','A1','A1','A1','A1',
         'A1','A1','A1','A1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','B1','B1','B1','B1',
         'B1','B1','B1','B1','B1','B1','B1','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2','A2',
         'A2','A2','A2','A2','A2','A2','A2','A2','A2','A2']


KMC_Result_current = types
# Conversion of "U" in 1 and "D" in 0 for display purposes
for j in range(len(KMC_Result_current)):
    if KMC_Result_current[j] == 'A1' or KMC_Result_current[j] == 'A2':
        KMC_Result_current[j] = 1
    if KMC_Result_current[j] == 'B1':
        KMC_Result_current[j] = 0
    
# Using islice to turn KMC_Result_current (list) in KMC_Result_current_matrix (100x100 matrix)
length_to_split = CONFIG_MATRIX_SIDE_SIZE * np.ones(CONFIG_MATRIX_SIDE_SIZE)
KMC_Result_current = iter(KMC_Result_current)
KMC_Result_current_matrix = [list(islice(KMC_Result_current, int(elem))) for elem in length_to_split]
KMC_Result_current_matrix = np.array(KMC_Result_current_matrix)
    
#Image display
#plt.figure()
plt.imshow(KMC_Result_current_matrix)
    
#Image saving in other directory
#plt.imsave(".\Images\Imtest%d.png" % i, KMC_Result_current_matrix)