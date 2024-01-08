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

# process 1 =  arrival of A type on an edge Si
elements_before_A_Si = ["A_Si", "Vt", "V"]
elements_after_A_Si = ["A_Si", "A_GaAs", "Vt"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 2.0]],
                                       elements_before=elements_before_A_Si,
                                       elements_after=elements_after_A_Si,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 2 = arrival of B type on Si
elements_before_B_Si = ["B_Si", "V"]
elements_after_B_Si = ["B_Si", "B_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_B_Si,
                                       elements_after=elements_after_B_Si,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 3 =  arrival of B type on an edge Si
elements_before_B_Si = ["B_Si", "Vt", "V"]
elements_after_B_Si = ["B_Si", "B_GaAs", "Vt"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 2.0]],
                                       elements_before=elements_before_B_Si,
                                       elements_after=elements_after_B_Si,
                                       basis_sites=[0],
                                       rate_constant=0.0))


# process 4 = arrival of A type on GaAs
elements_before_A_GaAs = ["A_GaAs", "V"]
elements_after_A_GaAs = ["A_GaAs", "A_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_A_GaAs,
                                       elements_after=elements_after_A_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 5 =  arrival of A type on  an edge GaAs
elements_before_A_GaAs = ["A_GaAs", "Vt", "V"]
elements_after_A_GaAs = ["A_GaAs", "A_GaAs", "Vt"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 2.0]],
                                       elements_before=elements_before_A_GaAs,
                                       elements_after=elements_after_A_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))


# process 6 = arrival of B type on GaAs
elements_before_B_GaAs = ["B_GaAs", "V"]
elements_after_B_GaAs = ["B_GaAs", "B_GaAs"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]],
                                       elements_before=elements_before_B_GaAs,
                                       elements_after=elements_after_B_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# process 7 =  arrival of A type on  an edge GaAs
elements_before_B_GaAs = ["B_GaAs", "Vt", "V"]
elements_after_B_GaAs = ["B_GaAs", "B_GaAs", "Vt"]

processes.append(KMCProcess(coordinates=[[0.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 0.0, 2.0]],
                                       elements_before=elements_before_B_GaAs,
                                       elements_after=elements_after_B_GaAs,
                                       basis_sites=[0],
                                       rate_constant=0.0))

# GaAs diffusion on Si

# GaAs diffusion on Si : number process in [8, 23] (16 processes)
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
        
        elements_before = [GaAs_type[j], "V", Si_type[j], "Vt"]
        elements_after = ["Vt", GaAs_type[j], Si_type[j], "V"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
# GaAs jumps from one monoatomic Si step to another (change of phase)
# No "Vt" states because jumps at the interfaces are already taking into account
# process_number in [24, 39]

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

# X_GaAs diffusion on X_GaAs : number process in [40, 55] (16 processes)
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
     
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
        elements_before = [GaAs_diffusion_dimere_type[j], "V", GaAs_underlayer_type[j], "Vt"]
        elements_after = ["Vt", GaAs_diffusion_dimere_type[j], GaAs_underlayer_type[j], "V"]
     
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))

# Y_GaAs diffusion on X_GaAs : number process in [55, 70] (16 processes)
# Change in GaAs phase A --> B

for i in range(len(list_of_coordinates)):
    
    elements_before = ["A_GaAs", "V", "B_GaAs", "V"]
    elements_after = ["V", "B_GaAs", "B_GaAs", "V"]
    
    processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                           elements_before=elements_before,
                                           elements_after=elements_after,
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
    elements_before = ["A_GaAs", "V", "B_GaAs", "Vt"]
    elements_after = ["Vt", "B_GaAs", "B_GaAs", "V"]
    
    processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                           elements_before=elements_before,
                                           elements_after=elements_after,
                                           basis_sites=[0],
                                           rate_constant=0.0))

# Change in GaAs phase B --> A

for i in range(len(list_of_coordinates)):
    
    elements_before = ["B_GaAs", "V", "A_GaAs", "V"]
    elements_after = ["V", "A_GaAs", "A_GaAs", "V"]
    
    processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                           elements_before=elements_before,
                                           elements_after=elements_after,
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
    elements_before = ["B_GaAs", "V", "A_GaAs", "Vt"]
    elements_after = ["Vt", "A_GaAs", "A_GaAs", "V"]
    
    processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                           elements_before=elements_before,
                                           elements_after=elements_after,
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
# X_GaAs jumps to a X_GaAs simple step (no phase change)
# process_number in [71, 102] (32 processes)

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
        
        elements_before = [GaAs_type[j], GaAs_type[j], "V", GaAs_type[j], "Vt"]
        elements_after = ["Vt", GaAs_type[j], GaAs_type[j], GaAs_type[j], "V"]
        
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
        
        elements_before = ["Vt", GaAs_type[j], GaAs_type[j], GaAs_type[j], "V"]
        elements_after = [GaAs_type[j], GaAs_type[j], "V", GaAs_type[j], "Vt"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))

# Y_GaAs jumps to a X_GaAs simple step (NO PHASE CHANGE)
# process_number in [103, 134] (32 processes)

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
        
        elements_before = [GaAs_type[j], GaAs_type[j], "V", GaAs_type_inverted[j], "Vt"]
        elements_after = ["Vt", GaAs_type[j], GaAs_type[j], GaAs_type_inverted[j], "V"]
        
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
        
        elements_before = ["Vt", GaAs_type_inverted[j], GaAs_type[j], GaAs_type[j], "V"]
        elements_after = [GaAs_type[j], GaAs_type_inverted[j], "V", GaAs_type[j], "Vt"]
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=elements_before,
                                               elements_after=elements_after,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
        
#########################
#    Interface moves    #
#########################

# interface diffusion on Si steps (un even number of step is required)
# process_number [135, 138]

list_of_coordinates = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 0.0, -2.0], [1.0, 0.0, 1.0], [1.0, 0.0, 2.0]]

Si_type = ["A_Si", "B_Si"]
GaAs_type = ["A_GaAs", "B_GaAs"]
GaAs_type_inverted = ["B_GaAs", "A_GaAs"]

for i in range(len(Si_type)):
    
    # go up on Si
    elements_before = ["V", Si_type[i], "Vt", GaAs_type_inverted[i], "V", "V"]
    elements_after = ["V", Si_type[i], "V", "Vt", GaAs_type[i], "V"]
            
    processes.append(KMCProcess(coordinates=list_of_coordinates,
                                elements_before=elements_before,
                                elements_after=elements_after,
                                basis_sites=[0],
                                rate_constant=0.0))
#[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, -1.0], [0.0, 0.0, -2.0], [1.0, 0.0, 1.0], [1.0, 0.0, 2.0]]
    
    # go down
    elements_before = ["V", Si_type[i], "V", "Vt", GaAs_type[i], "V"]
    elements_after = ["V", Si_type[i], "Vt", GaAs_type_inverted[i], "V", "V"]
            
    processes.append(KMCProcess(coordinates=list_of_coordinates,
                                elements_before=elements_before,
                                elements_after=elements_after,
                                basis_sites=[0],
                                rate_constant=0.0))

# diffuse at the interface on GaAs
# process_number [139, 144]

GaAs_type = ["A_GaAs", "B_GaAs"]
GaAs_type_inverted = ["B_GaAs", "A_GaAs"]

for i in range(len(GaAs_type)):
    
    for j in range(len(GaAs_type_inverted)):
        
        # go up on GaAs
        
        list_of_coordinates = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [1.0, 0.0, 1.0], [0.0, 0.0, -1.0], [0.0, 0.0, -2.0]]
    
        elements_before = ["V", GaAs_type_inverted[j], "V", "Vt", GaAs_type[i]]
        elements_after = ["V", GaAs_type_inverted[j], GaAs_type[i], "V", "Vt"]
                
        processes.append(KMCProcess(coordinates=list_of_coordinates,
                                    elements_before=elements_before,
                                    elements_after=elements_after,
                                    basis_sites=[0],
                                    rate_constant=0.0))
        
    # go down on GaAs
        
    list_of_coordinates = [[0.0, 0.0, 0.0], [1.0, 0.0, 1.0], [1.0, 0.0, 2.0], [0.0, 0.0, -1.0], [0.0, 0.0, -2.0]]
    
    elements_before = ["V", GaAs_type[i], "V", "V", "Vt"]
    elements_after = ["V", "V", "V", "Vt", GaAs_type[i]]
                
    processes.append(KMCProcess(coordinates=list_of_coordinates,
                                elements_before=elements_before,
                                elements_after=elements_after,
                                basis_sites=[0],
                                rate_constant=0.0))
        
# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
