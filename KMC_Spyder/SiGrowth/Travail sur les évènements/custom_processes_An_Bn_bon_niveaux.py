# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:52:10 2023

@author: msilvestre
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
config = KMCConfigurationFromScript("config_4_steps.py")

# Get the possible types from config
dictionnary_of_possible_types = config.possibleTypes()
#print dictionnary_of_possible_types
# Removal of generic '*' type from the dictionnary
del dictionnary_of_possible_types['*']
# Conversion of a dictionnary in the list of all entries
list_of_possible_types = dictionnary_of_possible_types.keys()
#print list_of_possible_types

sorted_list_of_possible_types = []
NumberOfTypes = len(list_of_possible_types)

# Get min height to sort list_of_possible_types

for i in range(NumberOfTypes):
    #print list_of_possible_types 
    min_height = int(list_of_possible_types[0][1])
    index = 0
    for j in range(len(list_of_possible_types)):
        current_height = int(list_of_possible_types[j][1])
        if current_height < min_height:
            min_height = current_height
            index = j
    sorted_list_of_possible_types.append(list_of_possible_types[index])
    del list_of_possible_types[index]

# sorted_list_of_possible_types --> list sorted from the lowest to the highest step

# List of all possible deplacement in 2 dimensions
    
# From elements_before point of view : list_of_coordinates = [right, left, forward, backward]
# From elements_after point of view : list_of_coordinates = [left, right, backward, forward]
list_of_coordinates = [[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0]]
                       ]

for a in range(len(sorted_list_of_possible_types)-2):

    #################################################
    #        Deposition of a quasi-dimere           #
    #################################################
    
    elements_before = sorted_list_of_possible_types[a]
    #print 'elements_before'
    #print elements_before
    
    elements_after = sorted_list_of_possible_types[a+1]
    #print 'elements_after'
    #print elements_after
    
    # All steps but the last one
    coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[elements_before],
                                           elements_after=[elements_after],
                                           basis_sites=[0],
                                           rate_constant=0.0))

    #################################################
    #         Diffusion of a quasi-dimere           #
    #################################################
    step_jump = sorted_list_of_possible_types[a+2]
    
    before_moving = [elements_after, elements_before]
    #print 'before_moving'
    #print before_moving
    
    after_moving = [elements_before, elements_after]
    #print 'after_moving'
    #print after_moving
    
    step_jumping = [elements_before, step_jump]
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=before_moving,
                                               elements_after=after_moving,
                                               basis_sites=[0],
                                               rate_constant=0.0))
    for i in range(len(list_of_coordinates)):   
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=before_moving,
                                               elements_after=step_jumping,
                                               basis_sites=[0],
                                               rate_constant=0.0))
    


# Last steps lead to the first ones (periodicity) (2 last steps linked to the 2 first)
for i in range(1,3):
    
    elements_before = sorted_list_of_possible_types[len(sorted_list_of_possible_types)-(3-i)]
    elements_after = sorted_list_of_possible_types[i]
    #print elements_before
    #print elements_after
    
    coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[elements_before],
                                           elements_after=[elements_after],
                                           basis_sites=[0],
                                           rate_constant=0.0))
    
    step_jump = sorted_list_of_possible_types[i+1]
    
    before_moving = [elements_after, elements_before]
    after_moving = [elements_before, elements_after]
    step_jumping = [elements_before, step_jump]
        
    for j in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                               elements_before=before_moving,
                                               elements_after=after_moving,
                                               basis_sites=[0],
                                               rate_constant=0.0))
    for j in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                               elements_before=before_moving,
                                               elements_after=step_jumping,
                                               basis_sites=[0],
                                               rate_constant=0.0))

#print len(processes)
# Create the interactions object.
interactions = KMCInteractions(processes, implicit_wildcards=True)
