# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:52:10 2023

@author: msilvestre

This program descibes all possible events that may happen during the KMC simulation
Contditions for them to happen are describes in the run program

for each step, there are the same possible events, there are listed in this order :
[dimere adsorption, forward, left, right, backward, jump forward, jump left, 
 jump right, jump backward]

This order is important for setting conditions in the run program

Rmq : this list is repeated for each step, in the run program you will need to 
use % 9 to know which process happen
"""

# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *

# List to store all processes
processes = []

# store the configuration to get all possibles types
config = KMCConfigurationFromScript("illustration_config.py")

# -----------------------------------------------------------------------
# List of all possible deplacement in 2 dimensions
    
#Atoms moves : [RIGHT, FORWARD, BACKWARD, LEFT, UPWARD, DOWNWARD]

# This move order is due to elements_before order in the custom rate calculator in the run program
list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                       [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                       [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0]]
                       ]

# Processes for GaAs-GaAs interactions
for i in range(len(list_of_coordinates)):
    
    coordinates = list_of_coordinates[i]
    
    elements_before = ["Si", "V"]
    elements_after = ["V", "Si"]
    
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=elements_before,
                                           elements_after=elements_after,
                                           basis_sites=[0],
                                           rate_constant=0.0))
 

# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
