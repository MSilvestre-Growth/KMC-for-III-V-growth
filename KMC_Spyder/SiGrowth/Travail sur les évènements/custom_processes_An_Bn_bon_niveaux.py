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
min_height = int(list_of_possible_types[0][1])
index = 0

for i in range(NumberOfTypes):
    for j in range(len(list_of_possible_types)):
        current_height = int(list_of_possible_types[j][1])
        if current_height < min_height:
            min_height = current_height
            index = j
    sorted_list_of_possible_types.append(list_of_possible_types[index])
    del list_of_possible_types[index]

# sorted_list_of_possible_types --> list sorted from the lowest to the highest step
print sorted_list_of_possible_types

#################################################
#        Deposition of a quasi-dimere           #
#################################################

for a in range(len(list_of_possible_types)):
    sites = list_of_possible_types[a]
    
    # A on B
    coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=['B'],
                                           elements_after=['A'],
                                           basis_sites=[0],
                                           rate_constant=1.0))
    
    # B on A
    coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=['A'],
                                           elements_after=['B'],
                                           basis_sites=[0],
                                           rate_constant=1.0))

#################################################
#         Diffusion of a quasi-dimere           #
#################################################

# List of all possible deplacement in 2 dimensions

# From 'A' point of view : list_of_coordinates = [right, left, forward, backward]
# From 'B' point of view : list_of_coordinates = [left, right, backward, forward]
list_of_coordinates = [[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0]]
                       ]

for i in range(len(list_of_coordinates)):
    processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                           elements_before=['A','B'],
                                           elements_after=['B','A'],
                                           basis_sites=[0],
                                           rate_constant=1.0))

# Create the interactions object.
interactions = KMCInteractions(processes, implicit_wildcards=True)
