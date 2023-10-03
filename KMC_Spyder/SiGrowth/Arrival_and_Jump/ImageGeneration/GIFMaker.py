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
for i in range(11):
      images.append(Image.open("C:/Users/msilvestre/Documents/GitHub/Images/SiGrowth/steps_4_test/Imtest%d.png" % i))
#GIF making

images[0].save('Si growth 0_16 seconde.gif',
           save_all = True, append_images = images[1:], 
           optimize = False, duration = 10)