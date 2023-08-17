# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:36:22 2023

@author: msilvestre
"""

# Copyright (c)  2014  Mikael Leetmaa
#
# This file is part of the KMCLib project distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#

from KMCLib import *

# ----------------------------------------------------------------------------
# Unit cell

cell_vectors = [[   1.000000e+00,   0.000000e+00,   0.000000e+00],
                [   0.000000e+00,   1.000000e+00,   0.000000e+00],
                [   0.000000e+00,   0.000000e+00,   1.000000e+00]]

basis_points = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]

unit_cell = KMCUnitCell(
    cell_vectors=cell_vectors,
    basis_points=basis_points)

# -----------------------------------------------------------------------------
# Lattice

lattice = KMCLattice(
    unit_cell=unit_cell,
    repetitions=(100,100,1),
    periodic=(True, True, False))

# -----------------------------------------------------------------------------
# Configuration

types = ['A1']*2500

for i in range(2500) :
    types.append('B2')
    
for j in range(2500) :
    types.append('A3')

for k in range(2500) :
    types.append('B4')

possible_types = ['A1','B2','A3','B4']
sorted_step = []

for i in range(len(possible_types)):
    #print possible_types 
    min_height = int(possible_types[0][1])
    index = 0
    for j in range(len(possible_types)):
        current_height = int(possible_types[j][1])
        if current_height < min_height:
            min_height = current_height
            index = j
    sorted_step.append(possible_types[index])
    del possible_types[index]

last_step =  sorted_step[len(sorted_step)-1]
last_step_type = last_step[0]
last_step_height = int(last_step[1])

# Add a new virtual highest step in the list
if last_step_type == "A":
    new_high_step = "B" + str(last_step_height+1)
    sorted_step.append(new_high_step)
if last_step_type == "B":
    new_high_step = "A" + str(last_step_height+1)
    sorted_step.append(new_high_step)
    
configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types=sorted_step)

# print tests
dictionnary_of_possible_types = configuration.possibleTypes()
print dictionnary_of_possible_types

list_of_possible_types = dictionnary_of_possible_types.keys()
del dictionnary_of_possible_types['*']
print list_of_possible_types
# end print tests

# Use the _script() function to get a script that can generate the configuration.
print "from KMCLib import *"
print configuration._script()
