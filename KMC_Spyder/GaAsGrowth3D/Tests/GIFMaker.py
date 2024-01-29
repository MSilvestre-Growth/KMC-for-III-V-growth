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
i = 0
for i in range(39):
      images.append(Image.open("C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Test 5/Imtest%d.png" % i))
#GIF making

images[0].save("C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Test 5/Results.gif",
           save_all = True, append_images = images[1:], 
           optimize = False, duration = 10)