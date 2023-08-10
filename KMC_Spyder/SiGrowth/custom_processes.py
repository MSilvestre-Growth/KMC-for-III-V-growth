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

# store the configuration to get all possibles types
config = KMCConfigurationFromScript("config_3_steps.py")

coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]

# Generic process = add a quasi-dimere on top of a layer, or remove a quasi-dimere
# from the top of a layer --> this has to be done for all the steps stored in config

# Get the possible types from config
dictionnary_of_possible_types = config.possibleTypes().keys()
# Removal of generic '*' type from the dictionnary
del dictionnary_of_possible_types['*']
# Conversion of a dictionnary in the list of all entries
list_of_possible_types = dictionnary_of_possible_types.keys()

# Get min and max height to respect types with the periodicity
max_height = int(list_of_possible_types[0][1])
min_heigth = int(list_of_possible_types[0][1])

for i in range(len(list_of_possible_types)):
    current_height = int(list_of_possible_types[i][1])
    if current_height > max_height:
        max_height = current_height
        type_of_highest_step = list_of_possible_types[i][0]
        
    if current_height < min_height:
        min_height = current_height
        type_of_lowest_step = list_of_possible_types[i][0]

print 'List of all processes :'
# Set each individual process in the processes list
for i in range(len(list_of_possible_types)):
    
    current_step = list_of_possible_types[i]
    current_type_of_step = current_step[0]
    current_height = int(current_step[1])
    
    if current_type_of_step == 'A':
        next_step_type = 'B'
    else:
        next_step_type = 'A'
    
    # Add a quasi-dimere on top of the current step
    
        # if statement to respect periodicity
    if current_height == max_height:
        next_height = min_height
        next_step_type = type_of_lowest_step
    else:
        next_height = str(current_height + 1)
    
        # Name of the new step
    next_step = next_step_type + next_height
    
    print 'Add a dimere on top of the current layer ' + current_step + ' --> ' + next_step
    processes.append(KMCProcess(coordinates=coordinates,
                       elements_before=[current_step],
                       elements_after=[next_step],
                       basis_sites=[0],
                       rate_constant=1.0))
    
    # Remove a quasi-dimere on top of the current step
    
        # if statement to respect periodicity
    if current_height == min_height:
        next_height = max_height
        next_step_type = type_of_highest_step
    else:
        next_height = str(current_height - 1)
        
        # Name of the new step
    next_step = next_step_type + next_height
    
    print 'Remove a dimere on top of the current layer ' + current_step + ' --> ' + next_step
    processes.append(KMCProcess(coordinates=coordinates,
                       elements_before=[current_step],
                       elements_after=[next_step],
                       basis_sites=[0],
                       rate_constant=1.0))

# Create the interactions object.
interactions = KMCInteractions(processes, implicit_wildcards=True)
