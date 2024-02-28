# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 10:58:39 2023

@author: msilvestre
"""

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#Stocking images from .\Images file
images = []
i,j,k = 0,0,0
for i in range(46):
      images.append(Image.open("C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Test 11 - jump anti-phase debug/part 1/Imtest%d.png" % i))

for j in range(48):
      images.append(Image.open("C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Test 11 - jump anti-phase debug/part 2/Imtest%d.png" % j))

for k in range(6):
      images.append(Image.open("C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Test 11 - jump anti-phase debug/part 3/Imtest%d.png" % k))

#GIF making

images[0].save("C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Arrival_test/Result.gif",
           save_all = True, append_images = images[1:], 
           optimize = False, duration = 10)