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
config = KMCConfigurationFromScript("illustration_config.py")

# Get the possible types from config
dictionnary_of_possible_types = config.possibleTypes()
#print dictionnary_of_possible_types

# Removal of generic '*' type from the dictionnary
del dictionnary_of_possible_types['*']

# Conversion of a dictionnary in the list of all entries
list_of_possible_types = dictionnary_of_possible_types.keys()
#print list_of_possible_types

# possible_types_Si_surface = all states from the initial Si surface
possible_types_Si_surface = []
NumberOfTypes = len(list_of_possible_types)

# Search elements to file possible_types_Si_surface list
for i in range(NumberOfTypes):
    index = 0
    if list_of_possible_types[i][-2]+list_of_possible_types[i][-1] == 'Si':
        possible_types_Si_surface.append(list_of_possible_types[i])    
        del list_of_possible_types[i]

# Add all GaAs steps to the Si steps    
sorted_list_of_possible_types = possible_types_Si_surface

for i in range(Number_of_possible_GaAs_steps):
    if i < 10 :
        prefixe = "0"
    else :
        prefixe = ""
    A_step_GaAs = "A" + prefixe + str(i) + "_GaAs"
    sorted_list_of_possible_types.append(A_step_GaAs)
    
    A_step_i_GaAs = "A" + prefixe + str(i) + "i_GaAs"
    sorted_list_of_possible_types.append(A_step_i_GaAs)
    
    B_step_GaAs = "B" + prefixe + str(i) + "_GaAs"
    sorted_list_of_possible_types.append(B_step_GaAs)
    
    B_step_i_GaAs = "B" + prefixe + str(i) + "i_GaAs"
    sorted_list_of_possible_types.append(B_step_i_GaAs)

print "test"
print sorted_list_of_possible_types

# -----------------------------------------------------------------------

##########################
#    Useful functions    #
##########################

# ---- general functions ----

# ex : n_plus_dimere_same_phase("A11", -1, sorted_list_of_possible_types) --> "A10"
def n_plus_dimere_same_phase(current_dimere, nth_atom_higher, list_of_states = sorted_list_of_possible_types):
    return list_of_states[current_dimere + 4 * nth_atom_higher]

# ex : n_plus_dimere_anti_phase("A11", 0, sorted_list_of_possible_types) --> "B11"
def n_plus_dimere_anti_phase(current_dimere, nth_atom_higher, list_of_states = sorted_list_of_possible_types):
    
    if list_of_states[current_dimere][0] == "A":
        return list_of_states[current_dimere + 4 * nth_atom_higher + 2]
    
    if list_of_states[current_dimere][0] == "B":
        return list_of_states[current_dimere + 4 * (nth_atom_higher - 1) + 2]

# ---- arrival functions ----
def f_upper_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, 2, list_of_states)

# ---- diffusion functions ----
    
# ex : f_underlying_surface_for_diffusion_same_phase("A11") --> "A09" (A natural underlying surface is odd by convention (see generation file))
# ex : f_underlying_surface_for_diffusion_same_phase("B11") --> "A09" (B natural surface is even by convention --> the underlying surface is the same than the "A11" case = "A09")
def f_underlying_surface_for_diffusion_same_phase(current_dimere, list_of_states = sorted_list_of_possible_types):
    # A odd case
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_same_phase(current_dimere, -2, list_of_states)
    
    # A even case
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_anti_phase(current_dimere, -2, list_of_states)
    
    # B odd case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_anti_phase(current_dimere, -2, list_of_states)
    
    # B even case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_same_phase(current_dimere, -2, list_of_states)

# ex : f_anti_phase_domain_1_down("A11") --> "B10" (A natural underlying surface is odd by convention --> lower anti-phase domain)
# ex : f_anti_phase_domain_1_down("B11") --> "B10" (B natural surface is even by convention --> the underlying surface is the same than the "A11" case = "A09")
def f_anti_phase_domain_1_down(current_dimere, list_of_states = sorted_list_of_possible_types):
    # A odd case = normal case, next layer need to be switch
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_anti_phase(current_dimere, -1, list_of_states)
    
    # A even case = anormal case, no need to be switch to B to go to lower domain
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_same_phase(current_dimere, -1, list_of_states)
    
    # B odd case = anormal case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_same_phase(current_dimere, -1, list_of_states)
    
    # B even case = normal case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_anti_phase(current_dimere, -1, list_of_states)


def f_diffusing_element(current_dimere, list_of_states = sorted_list_of_possible_types):
    # A odd case
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_same_phase(current_dimere, 0, list_of_states)
    
    # A even case
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_anti_phase(current_dimere, 0, list_of_states)
    
    # B odd case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_anti_phase(current_dimere, 0, list_of_states)
    
    # B even case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_same_phase(current_dimere, 0, list_of_states)

def f_anti_phase_domain_1_up(current_dimere, list_of_states = sorted_list_of_possible_types):
    # A odd case = normal case, next layer need to be switch
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_anti_phase(current_dimere, 1, list_of_states)
    
    # A even case = anormal case, no need to be switch to B to go to lower domain
    if list_of_states[current_dimere][0] == "A" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_same_phase(current_dimere, 1, list_of_states)
    
    # B odd case = anormal case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 1:
        return n_plus_dimere_same_phase(current_dimere, 1, list_of_states)
    
    # B even case = normal case
    if list_of_states[current_dimere][0] == "B" and int(list_of_states[current_dimere][1:3]) % 2 == 0:
        return n_plus_dimere_anti_phase(current_dimere, 1, list_of_states)
# ---- jumping functions ----
# if you jump from a domain to another, you keep your initial phase

# ex : simple_step_jumping_up_dimere("A11") = "A12"
def f_simple_step_jumping_up_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, 1, list_of_states)

# ex : simple_step_jumping_down_dimere("A11") = "A10"
def f_simple_step_jumping_down_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, -1, list_of_states)

# ex : double_step_jumping_up_dimere("A11") = "A13"
def f_double_step_jumping_up_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, 2, list_of_states)

# ex : double_step_jumping_down_dimere("A11") = "A09"
def f_double_step_jumping_down_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, -2, list_of_states)

# ex : triple_step_jumping_up_dimere("A11") = "A14"
def f_triple_step_jumping_up_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, 3, list_of_states)

# ex : triple_step_jumping_down_dimere("A11") = "A08"
def f_triple_step_jumping_down_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, -3, list_of_states)

# ex : quadruple_step_jumping_up_dimere("A11") = "A15"
def f_quadruple_step_jumping_up_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, 4, list_of_states)

# ex : quadruple_step_jumping_down_dimere("A11") = "A07"
def f_quadruple_step_jumping_down_dimere(current_dimere, list_of_states = sorted_list_of_possible_types):
    return n_plus_dimere_same_phase(current_dimere, -4, list_of_states)

# -----------------------------------------------------------------------
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
a = 0
processes_name_list = []

# Processes for GaAs-GaAs interactions
for a in range(6, len(sorted_list_of_possible_types)-20, 2):
    
    current_dimere = sorted_list_of_possible_types[a]
    current_dimere_interface = sorted_list_of_possible_types[a+1]
 
    #################################################
    #        Deposition of a quasi-dimere           #
    #################################################
    
    upper_dimere = f_upper_dimere(current_dimere)
    upper_dimere_interface = f_upper_dimere(current_dimere_interface)
    
    
    coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]
    
    # process_number = 0

    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[current_dimere],
                                           elements_after=[upper_dimere],
                                           basis_sites=[0],
                                           rate_constant=0.0))
 
    # Interface states
    # process_number = 1
    processes.append(KMCProcess(coordinates=coordinates,
                                           elements_before=[current_dimere_interface],
                                           elements_after=[upper_dimere_interface],
                                           basis_sites=[0],
                                           rate_constant=0.0))    
    
    #################################################
    #         Diffusion of a quasi-dimere           #
    #################################################
    
    diffusing_element = f_diffusing_element(current_dimere)
    underlying_surface_element_same_phase = f_underlying_surface_for_diffusion_same_phase(current_dimere)
    
    # Diffusion process, same phase
    # process_number = 2, 3, 4, 5
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[current_dimere, n_plus_dimere_same_phase(current_dimere, -2)],
                                               elements_after=[n_plus_dimere_same_phase(current_dimere, -2), current_dimere],
                                               basis_sites=[0],
                                               rate_constant=0.0))
    # Diffusion process, anti-phase
    # process_number = 6, 7, 8, 9
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[current_dimere, n_plus_dimere_anti_phase(current_dimere, -2)],
                                               elements_after=[n_plus_dimere_same_phase(current_dimere, -2), current_dimere],
                                               basis_sites=[0],
                                               rate_constant=0.0))
        
    # Jumping down single step
    # process_number = 6, 7, 8, 9
    
    anti_phase_domain_1_down = f_anti_phase_domain_1_down(current_dimere)
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[current_dimere, anti_phase_domain_1_down],
                                               elements_after=[underlying_surface_element_same_phase, n_plus_dimere_same_phase(current_dimere, -1)],
                                               basis_sites=[0],
                                               rate_constant=0.0))
    # Jumping up single step, to the same phase
    # process_number = 10, 11, 12, 13
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[current_dimere, n_plus_dimere_same_phase(current_dimere, -1)],
                                               elements_after=[n_plus_dimere_same_phase(current_dimere, -2), n_plus_dimere_same_phase(current_dimere, 1)],
                                               basis_sites=[0],
                                               rate_constant=0.0))
   # Jumping up single step, to the anti phase
   # process_number = 14, 15, 16, 17
   
   for i in range(len(list_of_coordinates)):
       processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                              elements_before=[current_dimere, n_plus_dimere_anti_phase(current_dimere, -1)],
                                              elements_after=[n_plus_dimere_same_phase(current_dimere, -2), n_plus_dimere_same_phase(current_dimere, 1)],
                                              basis_sites=[0],
                                              rate_constant=0.0))
       
    # Jumping down double step
    # process_number = 18, 19, 20, 21
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[current_dimere, n_plus_dimere_same_phase(current_dimere, -4)],
                                               elements_after=[n_plus_dimere_same_phase(current_dimere, -2), n_plus_dimere_same_phase(current_dimere, -2)],
                                               basis_sites=[0],
                                               rate_constant=0.0))
    
    # Jumping up double step
    # process_number = 18, 19, 20, 21
    
    for i in range(len(list_of_coordinates)):
        processes.append(KMCProcess(coordinates=list_of_coordinates[i],
                                               elements_before=[current_dimere, n_plus_dimere_same_phase(current_dimere, 2, list_of_states)],
                                               elements_after=[n_plus_dimere_same_phase(current_dimere, -2, list_of_states),  n_plus_dimere_same_phase(current_dimere, 4, list_of_states)],
                                               basis_sites=[0],
                                               rate_constant=0.0))
    # ATTENTION : j'ai pas les déplacements latéraux, à rajouter
    # ATTENTION à changer le nb de process dans le RUN

    # Déplacements normaux
    
    # Moving RIGHT at the interface
    # process_number = 14
    #print "process number = 14, 15, 16, 17"
    #print [elements_after_interface,elements_before_interface] ," to ",[elements_before_interface,elements_after_interface]

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
    #print "process number = 18, 19, 20, 21"
    #print [jumping_elements_interface, elements_before_interface] ," to ",[elements_after_interface, elements_after_interface]

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
    #print "process number = 22"
    #print [elements_after_interface, elements_after_interface] ," to ",[elements_before_interface, jumping_elements_interface]

    processes.append(KMCProcess(coordinates=list_of_coordinates[0],
                                elements_before=[elements_after_interface, elements_after_interface],
                                elements_after=[elements_before_interface, jumping_elements_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping FORWARD from the interface
    # process_number = 23
    #print "process number = 23"
    #print [elements_after_interface, elements_after] ," to ",[jumping_elements_interface, elements_before]

    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[elements_after_interface, elements_after],
                                elements_after=[jumping_elements_interface, elements_before],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Jumping BACKWARD from the interface
    # process_number = 24
    #print "process number = 24"
    #print [elements_after_interface, elements_after] ," to ",[elements_before_interface, jumping_elements]

    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[elements_after_interface, elements_after],
                                elements_after=[elements_before_interface, jumping_elements],
                                basis_sites=[0],
                                rate_constant=0.0))
   
    # Jumping LEFT at the interface
    # process_number = 25
    #print "process number = 25"
    #print [elements_after_interface, elements_after_interface] ," to ",[elements_before_interface, jumping_elements_interface]

    processes.append(KMCProcess(coordinates=list_of_coordinates[3],
                                elements_before=[elements_after_interface, elements_after_interface],
                                elements_after=[elements_before_interface, jumping_elements_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # Cycling process
    
    offset_cycling_step = Number_of_step_on_starting_surface * 2
    offset_moving_dimere = offset_cycling_step + 2
    
    offset_jumping_element_to_cycling_step = 2*2
    offset_jumping_element_to_interface = offset_moving_dimere + 2
    
    elements_of_current_step_interface = sorted_list_of_possible_types[a+1] 
    element_of_cycling_step = sorted_list_of_possible_types[a+offset_cycling_step]
    upper_step_moving_dimere = sorted_list_of_possible_types[a+offset_moving_dimere]  
    jumping_interface_element_to_cycling_step = sorted_list_of_possible_types[a+1+offset_jumping_element_to_cycling_step]
    jumping_element_to_interface = sorted_list_of_possible_types[a + offset_jumping_element_to_interface]
    #print "process number = 26"
    #print [elements_after_interface, element_of_cycling_step] ," to ",[elements_of_current_step_interface, upper_step_moving_dimere]


    # process_number = 26    
    processes.append(KMCProcess(coordinates=list_of_coordinates[1],
                                elements_before=[elements_after_interface, element_of_cycling_step],
                                elements_after=[elements_of_current_step_interface, upper_step_moving_dimere],
                                basis_sites=[0],
                                rate_constant=0.0))
        
    #print "process number = 27"
    #print [upper_step_moving_dimere, elements_of_current_step_interface] ," to ",[element_of_cycling_step, elements_after_interface]
        
    # process_number = 27
    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[upper_step_moving_dimere, elements_of_current_step_interface],
                                elements_after=[element_of_cycling_step, elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # process_number = 28
    processes.append(KMCProcess(coordinates=list_of_coordinates[1],
                                elements_before=[jumping_interface_element_to_cycling_step, element_of_cycling_step],
                                elements_after=[elements_after_interface, upper_step_moving_dimere],
                                basis_sites=[0],
                                rate_constant=0.0))
    
    # process_number = 29
    processes.append(KMCProcess(coordinates=list_of_coordinates[2],
                                elements_before=[jumping_element_to_interface, elements_of_current_step_interface],
                                elements_after=[upper_step_moving_dimere, elements_after_interface],
                                basis_sites=[0],
                                rate_constant=0.0))

# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
