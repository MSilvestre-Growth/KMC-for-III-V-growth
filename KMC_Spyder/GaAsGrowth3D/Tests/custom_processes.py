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
    

# Atom arrival on Si and GaAs

# process 0 =  arrival of A type on Si
elements_before_A_Si = ["A_Si", "V"]
elements_after_A_Si = ["A_Si", "A_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_A_Si,
                                       elements_after=elements_after_A_Si,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 1 = arrival of B type on Si
elements_before_B_Si = ["B_Si", "V"]
elements_after_B_Si = ["B_Si", "B_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_B_Si,
                                       elements_after=elements_after_B_Si,
                                       basis_sites=[0],
                                       rate_constant=0.0))


# process 2 = arrival of A type on GaAs
elements_before_A_GaAs = ["A_GaAs", "V"]
elements_after_A_GaAs = ["A_GaAs", "A_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_A_GaAs,
                                       elements_after=elements_after_A_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 3 = arrival of B type on GaAs
elements_before_B_GaAs = ["B_GaAs", "V"]
elements_after_B_GaAs = ["B_GaAs", "B_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_B_GaAs,
                                       elements_after=elements_after_B_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# GaAs diffusion on Si

# GaAs diffusion on Si : number process in [4, 11] (8 processes)
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
# process_number in [12, 27]

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
        
        # Jump down
        
        elements_before = [GaAs_type[j], Si_type[j], "V", Si_type_inverted[j], "V"]
        elements_after = ["V", Si_type[j], GaAs_type_inverted[j], Si_type_inverted[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
        # Jump up
        
        elements_before = ["V", Si_type[j], GaAs_type_inverted[j], Si_type_inverted[j], "V"]
        elements_after = [GaAs_type[j], Si_type[j], "V", Si_type_inverted[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
    

# GaAs diffusion on GaAs

# X_GaAs diffusion on X_GaAs : number process in [28, 35] (8 processes)
# Same GaAs species and no jumps --> no change in the GaAs type

list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, -1.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [-1.0, 0.0, -1.0], [0.0, 0.0, 1.0]]
                        ]


GaAs_underlayer_type = ["A_GaAs", "B_GaAs"]
GaAs_diffusion_dimere_type = ["A_GaAs", "B_GaAs"]

for i in range(len(list_of_coordinates)):
    for j in range(len(GaAs_underlayer_type)):
        
        elements_before = [GaAs_diffusion_dimere_type[j], "V", GaAs_underlayer_type[j], "V"]
        elements_after = ["V", GaAs_diffusion_dimere_type[j], GaAs_underlayer_type[j], "V"]
# 	print "liste coordinates ", len(list_of_coordinates[i])
# 	print "elements_before", len(elements_before)
# 	print "elements_after", len(elements_after)        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))

# Y_GaAs diffusion on X_GaAs : number process in [36, 43] (8 processes)
# Change in GaAs phase A --> B

elements_before = ["A_GaAs", "V", "B_GaAs", "V"]
elements_after = ["V", "B_GaAs", "B_GaAs", "V"]

for i in range(len(list_of_coordinates)):
    
    processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                           elements_before=elements_before,
                                           elements_after=elements_after,
                                           basis_sites=[0],
                                           rate_constant=0.0))

# Change in GaAs phase B --> A

elements_before = ["B_GaAs", "V", "A_GaAs", "V"]
elements_after = ["V", "A_GaAs", "A_GaAs", "V"]

for i in range(len(list_of_coordinates)):
    
    processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                           elements_before=elements_before,
                                           elements_after=elements_after,
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
# X_GaAs jumps to a X_GaAs simple step (no phase change)
# process_number in [44, 59] (16 processes)

list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, -1.0], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, -1.0], [0.0, -1.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [-1.0, 0.0, -2.0], [0.0, 0.0, 1.0]]
                        ]

GaAs_type = ["A_GaAs", "B_GaAs"]

for i in range(len(list_of_coordinates)):
    for j in range(len(GaAs_type)):
        
        # Jump down
        
        elements_before = [GaAs_type[j], GaAs_type[j], "V", GaAs_type[j], "V"]
        elements_after = ["V", GaAs_type[j], GaAs_type[j], GaAs_type[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
        # Jump up
        
        elements_before = ["V", GaAs_type[j], GaAs_type[j], GaAs_type[j], "V"]
        elements_after = [GaAs_type[j], GaAs_type[j], "V", GaAs_type[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))

# Y_GaAs jumps to a X_GaAs simple step (NO PHASE CHANGE)
# process_number in [60, 75] (16 processes)

list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, -1.0], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, -1.0], [0.0, -1.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, -2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [-1.0, 0.0, -2.0], [0.0, 0.0, 1.0]]
                        ]

GaAs_type = ["A_GaAs", "B_GaAs"]
GaAs_type_inverted = ["B_GaAs", "A_GaAs"]

for i in range(len(list_of_coordinates)):
    for j in range(len(GaAs_type)):
        
        # Jump down
        
        elements_before = [GaAs_type[j], GaAs_type[j], "V", GaAs_type_inverted[j], "V"]
        elements_after = ["V", GaAs_type[j], GaAs_type[j], GaAs_type_inverted[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
        # Jump up
        
        elements_before = ["V", GaAs_type_inverted[j], GaAs_type[j], GaAs_type[j], "V"]
        elements_after = [GaAs_type[j], GaAs_type_inverted[j], "V", GaAs_type[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
        
##########################
#    Interface states    #
##########################

# Atom arrival on Si and GaAs

# process 76 =  arrival of Ai type on Ai_ Si
elements_before_Ai_Si = ["Ai_Si", "V"]
elements_after_Ai_Si = ["Ai_Si", "Ai_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_Ai_Si,
                                       elements_after=elements_after_Ai_Si,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 77 = arrival of Bi type on Bi_Si
elements_before_Bi_Si = ["Bi_Si", "V"]
elements_after_Bi_Si = ["Bi_Si", "Bi_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_Bi_Si,
                                       elements_after=elements_after_Bi_Si,
                                       basis_sites=[0],
                                       rate_constant=0.0))


# process 78 = arrival of Ai type on Ai_GaAs
elements_before_Ai_GaAs = ["Ai_GaAs", "V"]
elements_after_Ai_GaAs = ["Ai_GaAs", "Ai_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_Ai_GaAs,
                                       elements_after=elements_after_Ai_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 79 = arrival of Bi type on Bi_GaAs
elements_before_Bi_GaAs = ["Bi_GaAs", "V"]
elements_after_Bi_GaAs = ["Bi_GaAs", "Bi_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_Bi_GaAs,
                                       elements_after=elements_after_Bi_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# i_GaAs diffusion on Si

# GaAs diffusion on Si : number process in [80, 89] (10 processes)
# Jumps are not allowed --> no change in the GaAs type
number_of_steps_in_config3D_f = float(number_of_steps_in_config3D)

# list_of_coordinates = [[[0.0, 0.0, 0.0], [1.0, 0.0, number_of_steps_in_config3D_f-1.0], [1.0, 0.0, number_of_steps_in_config3D_f-2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [-1.0, 0.0, -1.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, -1.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, -1.0, -1.0], [0.0, 0.0, 1.0]]
#                         ]

list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 0.0, 2.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [-1.0, 0.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, -1.0, -1.0], [0.0, 0.0, 1.0]]
                        ]

print list_of_coordinates
i_Si_type = ["Ai_Si", "Bi_Si"]
Si_type = ["A_Si", "B_Si"]

i_GaAs_type = ["Ai_GaAs", "Bi_GaAs"]
GaAs_type = ["A_GaAs", "B_GaAs"]

# What kind of cycle do we have on the stepped surface ? X-X or X-Y
if number_of_steps_in_config3D % 2 == 0:
    cycling_step_Si_type = ["B_Si", "A_Si"]
    cycling_step_GaAs_type = ["B_GaAs", "A_GaAs"]
    
if number_of_steps_in_config3D % 2 == 1:
   cycling_step_Si_type = ["A_Si", "B_Si"]
   cycling_step_GaAs_type = ["A_GaAs", "B_GaAs"]
   
for j in range(len(i_Si_type)):
    
    elements_before = []
    elements_after = []
    
    # # move forward = cycling step
    # elements_before.append([i_GaAs_type[j], "V", cycling_step_Si_type[j], "V"])
    # elements_after.append(["V", cycling_step_GaAs_type[j], cycling_step_Si_type[j], "V"])
    
    # move forward = cycling step
    elements_before.append([i_GaAs_type[j], "V", "V"])
    elements_after.append(["V", cycling_step_GaAs_type[j], "V"])    
    
    # move backward = i_GaAs transforms into GaAs
    elements_before.append([i_GaAs_type[j], "V", Si_type[j], "V"])
    elements_after.append(["V", GaAs_type[j], Si_type[j], "V"])
    
    # move right = no type changes
    elements_before.append([i_GaAs_type[j], "V", i_Si_type[j], "V"])
    elements_after.append(["V", i_GaAs_type[j], i_Si_type[j], "V"])
        
    # move left = no type changes
    elements_before.append([i_GaAs_type[j], "V", i_Si_type[j], "V"])
    elements_after.append(["V", i_GaAs_type[j], i_Si_type[j], "V"])
        
    for i in range(len(list_of_coordinates)):
            
            processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                                   elements_before=elements_before[i],
                                                   elements_after=elements_after[i],
                                                   basis_sites=[0],
                                                   rate_constant=0.0))
    print elements_before
    print elements_after
            
# Arrival from the surface on the interface (type change to interface)
list_of_coordinates = [[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, -1.0], [0.0, 0.0, 1.0]],
                        [[0.0, 0.0, 0.0], [-1.0, 0.0, -number_of_steps_in_config3D_f+1.0], [-1.0, 0.0, -number_of_steps_in_config3D_f], [0.0, 0.0, 1.0]],
                        ]

i_Si_type = ["Ai_Si", "Bi_Si"]
Si_type = ["A_Si", "B_Si"]

i_GaAs_type = ["Ai_GaAs", "Bi_GaAs"]
GaAs_type = ["A_GaAs", "B_GaAs"]

# What kind of cycle do we have on the stepped surface ? X-X or X-Y
if number_of_steps_in_config3D % 2 == 0:
    cycling_step_Si_type = ["B_Si", "A_Si"]
    cycling_step_GaAs_type = ["B_GaAs", "A_GaAs"]
    
if number_of_steps_in_config3D % 2 == 1:
   cycling_step_Si_type = ["A_Si", "B_Si"]
   cycling_step_GaAs_type = ["A_GaAs", "B_GaAs"]

for j in range(len(i_Si_type)):
    
    elements_before = []
    elements_after = []
    
    for i in range(len(list_of_coordinates)):
        
        # moving forward from a surface with the same height
        elements_before.append([GaAs_type[j], "V", i_Si_type[j], "V"])
        elements_after.append(["V", i_GaAs_type[j], i_Si_type[j], "V"])
        
        # moving from the cycling step
        elements_before.append([cycling_step_GaAs_type[j], "V", i_Si_type[j], "V"])
        elements_after.append(["V", i_GaAs_type[j], i_Si_type[j], "V"])
    
    for i in range(len(list_of_coordinates)):
            
            processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                                   elements_before=elements_before[i],
                                                   elements_after=elements_after[i],
                                                   basis_sites=[0],
                                                   rate_constant=0.0))
        
# # GaAs jumps from one monoatomic Si step to another (change of phase)
# # process_number in [12, 27]

# list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, -1.0], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, -1.0], [0.0, -1.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [-1.0, 0.0, -2.0], [0.0, 0.0, 1.0]]
#                         ]

# Si_type = ["A_Si", "B_Si"]
# Si_type_inverted = ["B_Si", "A_Si"]
# GaAs_type = ["A_GaAs", "B_GaAs"]
# GaAs_type_inverted = ["B_GaAs", "A_GaAs"]

# for i in range(len(list_of_coordinates)):
#     for j in range(len(Si_type)):
        
#         # Jump down
        
#         elements_before = [GaAs_type[j], Si_type[j], "V", Si_type_inverted[j], "V"]
#         elements_after = ["V", Si_type[j], GaAs_type_inverted[j], Si_type_inverted[j], "V"]
        
#         processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                                elements_before=elements_before,
#                                                elements_after=elements_after,
#                                                basis_sites=[0],
#                                                rate_constant=0.0))
        
#         # Jump up
        
#         elements_before = ["V", Si_type[j], GaAs_type_inverted[j], Si_type_inverted[j], "V"]
#         elements_after = [GaAs_type[j], Si_type[j], "V", Si_type_inverted[j], "V"]
        
#         processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                                elements_before=elements_before,
#                                                elements_after=elements_after,
#                                                basis_sites=[0],
#                                                rate_constant=0.0))
    

# # GaAs diffusion on GaAs

# # X_GaAs diffusion on X_GaAs : number process in [28, 35] (8 processes)
# # Same GaAs species and no jumps --> no change in the GaAs type

# list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 1.0, -1.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0], [0.0, -1.0, -1.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, -1.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [-1.0, 0.0, -1.0], [0.0, 0.0, 1.0]]
#                         ]


# GaAs_underlayer_type = ["A_GaAs", "B_GaAs"]
# GaAs_diffusion_dimere_type = ["A_GaAs", "B_GaAs"]

# for i in range(len(list_of_coordinates)):
#     for j in range(len(GaAs_underlayer_type)):
        
#         elements_before = [GaAs_diffusion_dimere_type[j], "V", GaAs_underlayer_type[j], "V"]
#         elements_after = ["V", GaAs_diffusion_dimere_type[j], GaAs_underlayer_type[j], "V"]
# 	print "liste coordinates ", len(list_of_coordinates[i])
# 	print "elements_before", len(elements_before)
# 	print "elements_after", len(elements_after)        
#         processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                                elements_before=elements_before,
#                                                elements_after=elements_after,
#                                                basis_sites=[0],
#                                                rate_constant=0.0))

# # Y_GaAs diffusion on X_GaAs : number process in [36, 43] (8 processes)
# # Change in GaAs phase A --> B

# elements_before = ["A_GaAs", "V", "B_GaAs", "V"]
# elements_after = ["V", "B_GaAs", "B_GaAs", "V"]

# for i in range(len(list_of_coordinates)):
    
#     processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                            elements_before=elements_before,
#                                            elements_after=elements_after,
#                                            basis_sites=[0],
#                                            rate_constant=0.0))

# # Change in GaAs phase B --> A

# elements_before = ["B_GaAs", "V", "A_GaAs", "V"]
# elements_after = ["V", "A_GaAs", "A_GaAs", "V"]

# for i in range(len(list_of_coordinates)):
    
#     processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                            elements_before=elements_before,
#                                            elements_after=elements_after,
#                                            basis_sites=[0],
#                                            rate_constant=0.0))
    
# # X_GaAs jumps to a X_GaAs simple step (no phase change)
# # process_number in [44, 59] (16 processes)

# list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, -1.0], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, -1.0], [0.0, -1.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [-1.0, 0.0, -2.0], [0.0, 0.0, 1.0]]
#                         ]

# GaAs_type = ["A_GaAs", "B_GaAs"]

# for i in range(len(list_of_coordinates)):
#     for j in range(len(GaAs_type)):
        
#         # Jump down
        
#         elements_before = [GaAs_type[j], GaAs_type[j], "V", GaAs_type[j], "V"]
#         elements_after = ["V", GaAs_type[j], GaAs_type[j], GaAs_type[j], "V"]
        
#         processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                                elements_before=elements_before,
#                                                elements_after=elements_after,
#                                                basis_sites=[0],
#                                                rate_constant=0.0))
        
#         # Jump up
        
#         elements_before = ["V", GaAs_type[j], GaAs_type[j], GaAs_type[j], "V"]
#         elements_after = [GaAs_type[j], GaAs_type[j], "V", GaAs_type[j], "V"]
        
#         processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                                elements_before=elements_before,
#                                                elements_after=elements_after,
#                                                basis_sites=[0],
#                                                rate_constant=0.0))

# # Y_GaAs jumps to a X_GaAs simple step (NO PHASE CHANGE)
# # process_number in [60, 75] (16 processes)

# list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 1.0, -1.0], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, -1.0, -1.0], [0.0, -1.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [1.0, 0.0, -1.0], [1.0, 0.0, -2.0], [0.0, 0.0, 1.0]],
#                         [[0.0, 0.0, 0.0], [0.0, 0.0, -1.0], [-1.0, 0.0, -1.0], [-1.0, 0.0, -2.0], [0.0, 0.0, 1.0]]
#                         ]

# GaAs_type = ["A_GaAs", "B_GaAs"]
# GaAs_type_inverted = ["B_GaAs", "A_GaAs"]

# for i in range(len(list_of_coordinates)):
#     for j in range(len(GaAs_type)):
        
#         # Jump down
        
#         elements_before = [GaAs_type[j], GaAs_type[j], "V", GaAs_type_inverted[j], "V"]
#         elements_after = ["V", GaAs_type[j], GaAs_type[j], GaAs_type_inverted[j], "V"]
        
#         processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                                elements_before=elements_before,
#                                                elements_after=elements_after,
#                                                basis_sites=[0],
#                                                rate_constant=0.0))
        
#         # Jump up
        
#         elements_before = ["V", GaAs_type_inverted[j], GaAs_type[j], GaAs_type[j], "V"]
#         elements_after = [GaAs_type[j], GaAs_type_inverted[j], "V", GaAs_type[j], "V"]
        
#         processes.append(KMCProcess(coordinates=list_of_coordinates[i],
#                                                elements_before=elements_before,
#                                                elements_after=elements_after,
#                                                basis_sites=[0],
#                                                rate_constant=0.0))
        
# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
