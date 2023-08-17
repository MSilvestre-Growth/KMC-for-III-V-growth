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

# List of all possible deplacement in 2 dimensions
    
# From elements_before point of view : list_of_coordinates = [forward, left, right, backward]
# From elements_after point of view : list_of_coordinates = [left, right, backward, forward]
# This move order is due to elements_before order in the custom rate calculator in the run program
list_of_coordinates = [[[0.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
                       [[0.0, 0.0, 0.0], [-1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0], [0.0, -1.0, 0.0]]
                       ]

# Jump from one step to the other requires 2 higher states from the lower
# step point of view, that explain the folowing chosen range
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
    
    # Movement on a step
    before_moving = [elements_after, elements_before]
    #print 'before_moving'
    #print before_moving
    
    after_moving = [elements_before, elements_after]
    #print 'after_moving'
    #print after_moving
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=before_moving,
                                               elements_after=after_moving,
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
    # Movement from a step to the one below it
    step_jump = sorted_list_of_possible_types[a+2]    
    before_jump = [elements_before, step_jump]
    step_jumping = [elements_after, elements_after]
    
    # print "elements_before"
    # print elements_before
       
    # print "elements_after"
    # print elements_after

    # print "step_jump"
    # print step_jump

    for i in range(len(list_of_coordinates)):   
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=before_jump,
                                               elements_after=step_jumping,
                                               basis_sites=[0],
                                               rate_constant=0.0))
    


# Last steps lead to the first ones (periodicity) (2 last steps linked to the 2 first)
# Rmq : this periodicity may lead to problem in conditions for events to happen
# that is why we have added supplementary steps in generate_config.py

# before last step
    
elements_before = sorted_list_of_possible_types[len(sorted_list_of_possible_types)-2]
elements_after = sorted_list_of_possible_types[len(sorted_list_of_possible_types)-1]
#print elements_before
#print elements_after
    
coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
processes.append(KMCProcess(coordinates=coordinates,
                                       elements_before=[elements_before],
                                       elements_after=[elements_after],
                                       basis_sites=[0],
                                       rate_constant=0.0))
    
step_jump = sorted_list_of_possible_types[0]

before_moving = [elements_after, elements_before]
after_moving = [elements_before, elements_after]
before_jump = [elements_before, step_jump]
step_jumping = [elements_after, elements_after]
       
# print "elements_before"
# print elements_before
       
# print "elements_after"
# print elements_after

# print "step_jump"
# print step_jump

for j in range(len(list_of_coordinates)):
    processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                           elements_before=before_moving,
                                           elements_after=after_moving,
                                           basis_sites=[0],
                                           rate_constant=0.0))
for j in range(len(list_of_coordinates)):
    processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                           elements_before=before_jump,
                                           elements_after=step_jumping,
                                           basis_sites=[0],
                                           rate_constant=0.0))

# last step
    
elements_before = sorted_list_of_possible_types[len(sorted_list_of_possible_types)-1]
elements_after = sorted_list_of_possible_types[0]
#print elements_before
#print elements_after
    
coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
processes.append(KMCProcess(coordinates=coordinates,
                                       elements_before=[elements_before],
                                       elements_after=[elements_after],
                                       basis_sites=[0],
                                       rate_constant=0.0))
    
step_jump = sorted_list_of_possible_types[1]

before_moving = [elements_after, elements_before]
after_moving = [elements_before, elements_after]
before_jump = [elements_before, step_jump]
step_jumping = [elements_after, elements_after]

# print "elements_before"
# print elements_before
       
# print "elements_after"
# print elements_after

# print "step_jump"
# print step_jump

for j in range(len(list_of_coordinates)):
    processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                           elements_before=before_moving,
                                           elements_after=after_moving,
                                           basis_sites=[0],
                                           rate_constant=0.0))
for j in range(len(list_of_coordinates)):
    processes.append(KMCProcess(coordinates=list_of_coordinates[j],
                                           elements_before=before_jump,
                                           elements_after=step_jumping,
                                           basis_sites=[0],
                                           rate_constant=0.0))

#print len(processes)

# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
