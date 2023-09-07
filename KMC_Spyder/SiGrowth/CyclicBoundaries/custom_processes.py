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

############################################################################
#    WARNING : don't modify anything unless you know what you are doing    #
############################################################################

from KMCLib import *

# List to store all processes
processes = []

# store the configuration to get all possibles types
config = KMCConfigurationFromScript("config_4_steps_interface.py")

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
    min_height = int(list_of_possible_types[0][1])
    index = 0
    for j in range(len(list_of_possible_types)):
        current_height = int(list_of_possible_types[j][1])
        if current_height <= min_height and len(list_of_possible_types[j]) == 2:
            min_height = current_height
            index = j
        if current_height <= min_height and len(list_of_possible_types[j]) == 3:
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

a,b = 0,0

while a < len(sorted_list_of_possible_types)-3:
 
    #################################################
    #        Deposition of a quasi-dimere           #
    #################################################
    
    elements_before = sorted_list_of_possible_types[a]
    #print 'elements_before'
    #print elements_before
    
    elements_before_interface = sorted_list_of_possible_types[a+1]
    
    elements_after = sorted_list_of_possible_types[a+2]
    #print 'elements_after'
    #print elements_after
    
    elements_after_interface = sorted_list_of_possible_types[a+3]
    
    # All steps but the last one
    coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
    #print b
    #b += 1
    #print elements_before + ' --> ' + elements_after 
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[elements_before],
                                           elements_after=[elements_after],
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
    #print b
    #b += 1
    #print elements_before_interface + ' --> ' + elements_after_interface
 
    # Interface states
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[elements_before_interface],
                                           elements_after=[elements_after_interface],
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
    #################################################
    #         Diffusion of a quasi-dimere           #
    #################################################
    
    # Movement on a step
    before_moving = [elements_after, elements_before]
    #print 'before_moving'
    #print before_moving
    
    before_moving_interface = [elements_after, elements_before_interface]
    
    after_moving = [elements_before, elements_after]
    #print 'after_moving'
    #print after_moving
    
    after_moving_interface = [elements_before, elements_after_interface]
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=before_moving,
                                               elements_after=after_moving,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=before_moving_interface,
                                               elements_after=after_moving_interface,
                                               basis_sites=[0],
                                               rate_constant=0.0))

    a += 2
    print a

# Last steps lead to the first ones (periodicity)
# Rmq : this periodicity may lead to problem in conditions for events to happen
# that is why we have added supplementary steps in generate_config.py

# last step
    
elements_before = sorted_list_of_possible_types[len(sorted_list_of_possible_types)-2]
elements_before_interface = sorted_list_of_possible_types[len(sorted_list_of_possible_types)-1]

elements_after = sorted_list_of_possible_types[0]
elements_after_interface = sorted_list_of_possible_types[1]
print elements_before
print elements_after


before_moving = [elements_after, elements_before]
after_moving = [elements_before, elements_after]

before_moving_interface = [elements_after, elements_before_interface]
after_moving_interface = [elements_before, elements_after_interface]

    
coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
processes.append(KMCProcess(coordinates=coordinates,
                                       elements_before=[elements_before],
                                       elements_after=[elements_after],
                                       basis_sites=[0],
                                       rate_constant=0.0))

processes.append(KMCProcess(coordinates=coordinates,
                                       elements_before=[elements_before_interface],
                                       elements_after=[elements_after_interface],
                                       basis_sites=[0],
                                       rate_constant=0.0))
    
for j in range(len(list_of_coordinates)):
    processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                           elements_before=before_moving,
                                           elements_after=after_moving,
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
    processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                           elements_before=before_moving_interface,
                                           elements_after=after_moving_interface,
                                           basis_sites=[0],
                                           rate_constant=0.0))

print len(processes)

# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
