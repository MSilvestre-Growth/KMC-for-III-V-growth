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

number_of_steps_in_config3D = 4

# List to store all processes
processes = []

# store the configuration to get all possibles types
config = KMCConfigurationFromScript("config3D.py")

# -----------------------------------------------------------------------
# List of all possible deplacements

# GaAs diffusion on Si

# GaAs diffusion on Si :
# Jumps are not allowed --> no change in the GaAs type

list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, -1.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [-1.0, 0.0, -1.0], [0.0, 0.0, 1.0]]
                        ]

Si_type = ["A_Si", "B_Si"]
GaAs_type = ["A_GaAs", "B_GaAs"]

for i in range(len(list_of_coordinates)):
    for j in range(len(Si_type)):
        
        elements_before = [GaAs_type[j], "V", Si_type[j], "V"]
        elements_after = ["V", GaAs_type[j], Si_type[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
# GaAs jumps from one monoatomic Si step to another (change of phase)

list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, -1.0], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, -1.0], [0.0, -1.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [-1.0, 0.0, -2.0], [0.0, 0.0, 1.0]]
                        ]

Si_type = ["A_Si", "B_Si"]
Si_type_inverted = ["B_Si", "A_Si"]
GaAs_type = ["A_GaAs", "B_GaAs"]
GaAs_type_inverted = ["B_GaAs", "A_GaAs"]

for i in range(len(list_of_coordinates)):
    for j in range(len(Si_type)):
        
        # go down
        
        elements_before = [GaAs_type[j], Si_type[j], "V", Si_type_inverted[j], "V"]
        elements_after = ["V", Si_type[j], GaAs_type_inverted[j], Si_type_inverted[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                                elements_before=elements_before,
                                                elements_after=elements_after,
                                                basis_sites=[0],
                                                rate_constant=0.0))
        
        # go up
        
        elements_before = ["V", Si_type[j], GaAs_type_inverted[j], Si_type_inverted[j], "V"]
        elements_after = [GaAs_type[j], Si_type[j], "V", Si_type_inverted[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                                elements_before=elements_before,
                                                elements_after=elements_after,
                                                basis_sites=[0],
                                                rate_constant=0.0))
        
# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
