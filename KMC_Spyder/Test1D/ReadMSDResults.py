# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:04:29 2023

@author: msilvestre
"""

import matplotlib.pyplot as plt
import numpy as np

MSD = []
TIME = []

with open('msd.data', 'r') as f:
    
    lines = f.readlines()
    names=[]
    data=[[],[]]
    compteur = 0
    
    for x in lines:
        # on passe les 2 premières lignes de texte et la dernière ligne qui est ';; \n'
        if compteur == 0 :
            pass
        else:
            x_split = x.split(' ')
            MSD.append(float(x_split[0]))
            TIME.append(float(x_split[1]))
            
        compteur += 1
            
MSD = np.asarray(MSD)
TIME = np.asarray(TIME)
f.close()

plt.plot(MSD, TIME)
plt.show()
              