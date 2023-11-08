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
for i in range(101 - 23):
      j = i + 23
      images.append(Image.open("C:/Users/msilvestre/Documents/GitHub/Images/SiGrowth/steps_4_test/Results_steps_8e+07_Flux_2_T°C_950_En_0.05_Ep_0.5/Imtest%d.png" % j))
#GIF making

images[0].save("C:/Users/msilvestre/Documents/GitHub/Images/SiGrowth/steps_4_test/Results_steps_8e+07_Flux_2_T°C_950_En_0.05_Ep_0.5/Si growth 950K step flow.gif",
           save_all = True, append_images = images[1:], 
           optimize = False, duration = 10)