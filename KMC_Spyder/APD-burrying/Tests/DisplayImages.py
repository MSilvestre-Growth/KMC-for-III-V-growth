# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:36:48 2023

@author: msilvestre
"""

import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from PIL import Image

types = ['A1']*200
for i in range(200) :
    types.append('B1')


KMC_Result_current = types
# Conversion of "U" in 1 and "D" in 0 for display purposes
for j in range(len(KMC_Result_current)):
    if KMC_Result_current[j] == 'A1':
        KMC_Result_current[j] = 1
    if KMC_Result_current[j] == 'B1':
        KMC_Result_current[j] = 0
    
# Using islice to turn KMC_Result_current (list) in KMC_Result_current_matrix (100x100 matrix)
length_to_split = 20 * np.ones(20)
KMC_Result_current = iter(KMC_Result_current)
KMC_Result_current_matrix = [list(islice(KMC_Result_current, int(elem))) for elem in length_to_split]
KMC_Result_current_matrix = np.array(KMC_Result_current_matrix)
    
#Image display
#plt.figure()
plt.imshow(KMC_Result_current_matrix)
    
#Image saving in other directory
#plt.imsave(".\Images\Imtest%d.png" % i, KMC_Result_current_matrix)