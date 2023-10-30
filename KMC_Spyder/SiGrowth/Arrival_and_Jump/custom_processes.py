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


Number_of_step_on_starting_surface = 4



############################################################################
#    WARNING : don't modify anything unless you know what you are doing    #
############################################################################

from KMCLib import *

# List to store all processes
processes = []

# store the configuration to get all possibles types
config = KMCConfigurationFromScript("config_4_steps.py")

# Get the possible types from config
dictionnary_of_possible_types = config.possibleTypes()
#print dictionnary_of_possible_types

# Removal of generic '*' type from the dictionnary
del dictionnary_of_possible_types['*']

# Conversion of a dictionnary in the list of all entries
list_of_possible_types = dictionnary_of_possible_types.keys()
#print list_of_possible_types

# sorted_list_of_possible_types --> list sorted from the lowest to the highest step
sorted_list_of_possible_types = []
NumberOfTypes = len(list_of_possible_types)

# Get min height to sort list_of_possible_types
for i in range(NumberOfTypes/2):
    #print list_of_possible_types 
    min_height = int(list_of_possible_types[0][1:3])
    index = 0
    for j in range(len(list_of_possible_types)):
        current_height = int(list_of_possible_types[j][1:3])
        if current_height <= min_height and len(list_of_possible_types[j]) == 3:
            min_height = current_height
            index = j
        if current_height <= min_height and len(list_of_possible_types[j]) == 4:
            min_height = current_height
            index_interface = j

    del1 = list_of_possible_types[index]
    del2 = list_of_possible_types[index_interface]

    sorted_list_of_possible_types.append(del1)
    sorted_list_of_possible_types.append(del2)
    
    list_of_possible_types.remove(del1)
    list_of_possible_types.remove(del2)
    
# Exemple of sorted_list_of_possible_types with interface states just after
# corresponding states :
# sorted_list_of_possible_types ==
# ['A1', 'A1i', 'B2', 'B2i', 'A3', 'A3i', 'B4', 'B4i', 'A5', 'A5i', 'B6', 'B6i']

# List of all possible deplacement in 2 dimensions
    
#Atoms moves : [RIGHT, FORWARD, BACKWARD, LEFT]

# This move order is due to elements_before order in the custom rate calculator in the run program
list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                       [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0]]
                       ]

# Deposition requires to look at 1 step higher tha the current one
# --> -2 = 1 for the higher one + 1 for the higher one in the interface case
# we go 2 by 2 because we considers normal and interface ceses in the same loop

#print sorted_list_of_possible_types

#for a in range(0, len(sorted_list_of_possible_types)-2, 2):

# a is starting at -4 to allow cycling definition of processes in the loops
# (otherwise we would need 2 other single loops to define diffusion and jumps)
a = 0
processes_name_list = []

max_height = int(sorted_list_of_possible_types[len(sorted_list_of_possible_types)-2][1:3])

while a < len(sorted_list_of_possible_types)-10:
 
    #################################################
    #        Deposition of a quasi-dimere           #
    #################################################
    
    elements_before = sorted_list_of_possible_types[a]
    elements_before_interface = sorted_list_of_possible_types[a+1]
    
    elements_after = sorted_list_of_possible_types[a+2]    
    elements_after_interface = sorted_list_of_possible_types[a+3]
    
    jumping_elements = sorted_list_of_possible_types[a+4]
    jumping_elements_interface = sorted_list_of_possible_types[a+5]
    
    # All steps but the last one
    coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
    
    # process_number = 0
    print "process number = 0, 1"
    print [elements_before] ," to ",[elements_after]

    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[elements_before],
                                           elements_after=[elements_after],
                                           basis_sites=[0],
                                           rate_constant=0.0))
 
    # Interface states
    #print elements_before_interface
    #print elements_after_interface
    
    # process_number = 1
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[elements_before_interface],
                                           elements_after=[elements_after_interface],
                                           basis_sites=[0],
                                           rate_constant=0.0))    
    
    #################################################
    #         Diffusion of a quasi-dimere           #
    #################################################
    
    # process_number = 2, 3, 4, 5
    print "process number = 2, 3, 4, 5"
    print [elements_after, elements_before] ," to ",[elements_before, elements_after]
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[elements_after, elements_before],
                                               elements_after=[elements_before, elements_after] ,
                                               basis_sites=[0],
                                               rate_constant=0.0))
    
    # Jumping down
    # process_number = 6, 7, 8, 9
    print "process number = 6, 7, 8, 9"
    print [jumping_elements, elements_before] ," to ",[elements_after, elements_after]
   
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[jumping_elements, elements_before],
                                               elements_after=[elements_after, elements_after],
                                               basis_sites=[0],
                                               rate_constant=0.0))
    # Jumping up
    # process_number = 10, 11, 12, 13
    print "process number = 10, 11, 12, 13"
    print [elements_after, elements_after] ," to ",[elements_before, jumping_elements]
  
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[elements_after, elements_after],
                                               elements_after=[elements_before, jumping_elements],
                                               basis_sites=[0],
                                               rate_constant=0.0))
   
    # ATTENTION : j'ai pas les déplacements latéraux, à rajouter
    # ATTENTION à changer le nb de process dans le RUN

    # Déplacements normaux
    
    # Moving RIGHT at the interface
    # process_number = 14
    print "process number = 14, 15, 16, 17"
    print [elements_after_interface,elements_before_interface] ," to ",[elements_before_interface,elements_after_interface]

    processes.append(KMCProcess(coordinates=list_of_coordinates[0],
                                elements_before=[elements_after_interface,elements_before_interface],
                                elements_after=[elements_before_interface,elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Moving FORWARD to the interface
    # process_number = 15
    processes.append(KMCProcess(coordinates=list_of_coordinates[1],
                                elements_before=[elements_after, elements_before_interface],
                                elements_after=[elements_before, elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Moving BACKWARD from the interface
    # process_number = 16
    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[elements_after_interface,elements_before],
                                elements_after=[elements_before_interface,elements_after],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Moving LEFT at the interface
    # process_number = 17
    processes.append(KMCProcess(coordinates=list_of_coordinates[3],
                                elements_before=[elements_after_interface,elements_before_interface],
                                elements_after=[elements_before_interface,elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping DOWN at the interface
    
    # Jumping RIGHT at the interface
    # process_number = 18
    print "process number = 18, 19, 20, 21"
    print [jumping_elements_interface, elements_before_interface] ," to ",[elements_after_interface, elements_after_interface]

    processes.append(KMCProcess(coordinates=list_of_coordinates[0],
                                elements_before=[jumping_elements_interface, elements_before_interface],
                                elements_after=[elements_after_interface, elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping FORWARD from the interface
    # process_number = 19
    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[elements_before_interface, jumping_elements],
                                elements_after=[elements_after_interface, elements_after],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping BACKWARD from the interface
    # process_number = 20
    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[jumping_elements_interface, elements_before],
                                elements_after=[elements_after_interface, elements_after],
                                basis_sites=[0],
                                rate_constant=0.0))
   
    # Jumping LEFT at the interface
    # process_number = 21
    processes.append(KMCProcess(coordinates=list_of_coordinates[3],
                                elements_before=[jumping_elements_interface, elements_before_interface],
                                elements_after=[elements_after_interface, elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping UP at the interface
    
    # Jumping RIGHT at the interface
    # process_number = 22
    print "process number = 22"
    print [elements_after_interface, elements_after_interface] ," to ",[elements_before_interface, jumping_elements_interface]

    processes.append(KMCProcess(coordinates=list_of_coordinates[0],
                                elements_before=[elements_after_interface, elements_after_interface],
                                elements_after=[elements_before_interface, jumping_elements_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping FORWARD from the interface
    # process_number = 23
    print "process number = 23"
    print [elements_after_interface, elements_after] ," to ",[jumping_elements_interface, elements_before]

    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[elements_after_interface, elements_after],
                                elements_after=[jumping_elements_interface, elements_before],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping BACKWARD from the interface
    # process_number = 24
    print "process number = 24"
    print [elements_after_interface, elements_after] ," to ",[elements_before_interface, jumping_elements]

    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[elements_after_interface, elements_after],
                                elements_after=[elements_before_interface, jumping_elements],
                                basis_sites=[0],
                                rate_constant=0.0))
   
    # Jumping LEFT at the interface
    # process_number = 25
    print "process number = 25"
    print [elements_after_interface, elements_after_interface] ," to ",[elements_before_interface, jumping_elements_interface]

    processes.append(KMCProcess(coordinates=list_of_coordinates[3],
                                elements_before=[elements_after_interface, elements_after_interface],
                                elements_after=[elements_before_interface, jumping_elements_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Cycling process
    
    offset_cycling_step = Number_of_step_on_starting_surface * 2
    offset_moving_dimere = offset_cycling_step + 2
   
    
    elements_of_current_step_interface = sorted_list_of_possible_types[a+1] 
    element_of_cycling_step = sorted_list_of_possible_types[a+offset_cycling_step]
    upper_step_moving_dimere = sorted_list_of_possible_types[a+offset_moving_dimere]  
   
    print "process number = 26"
    print [elements_after_interface, element_of_cycling_step] ," to ",[elements_of_current_step_interface, upper_step_moving_dimere]


    # process_number = 26    
    processes.append(KMCProcess(coordinates=list_of_coordinates[1],
                                elements_before=[elements_after_interface, element_of_cycling_step],
                                elements_after=[elements_of_current_step_interface, upper_step_moving_dimere],
                                basis_sites=[0],
                                rate_constant=0.0))
        
    print "process number = 27"
    print [upper_step_moving_dimere, elements_of_current_step_interface] ," to ",[element_of_cycling_step, elements_after_interface]
        
    # process_number = 27
    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[upper_step_moving_dimere, elements_of_current_step_interface],
                                elements_after=[element_of_cycling_step, elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    
    a += 2

# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
