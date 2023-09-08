# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:36:22 2023

@author: msilvestre

The goal of this program is to generate a starting surface for the KMC simulation

running command :
python2 generate_config_4_steps.py > config_4_steps.py
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

################################################################################
#    User zone : define the size and the periodicity of your simulated zone    #
################################################################################

# Precise the number of pixel in each direction (at least 1)
X = 25
Y = 100 
Z = 1

# Precise if you want your structure to be periodic in different directions
# (True or False)
X_periodic = True
Y_periodic = True
Z_periodic = False

# Setting of the lattice with previous informations
lattice = KMCLattice(
    unit_cell=unit_cell,
    repetitions=(X,Y,Z),
    periodic=(X_periodic, Y_periodic, Z_periodic))

# -----------------------------------------------------------------------------
# Configuration

##################################################
#    User Zone : define your starting surface    #
##################################################

# types is a SIMPLE list which must contain X * Y elements
# the position in the XxY matrix can be deduce by the position p in types list
# as following :
# let (q,r) be the euclidian of p by X i.e. p = q*X+r
# then position in the XxY mattrix is (x,y) = (q, r) rmq : matrix index begin at 0

# writting of starting surface

# interface line for cyclic boundaries
types = ['A1i']*100

for h in range(2400) :
    types.append('A1')

# write all possibles types that you entered previously
possible_types = ['A1']

# We want to define supplementary steps to be coherent with our step notation
# and atomic processes describes in custom process
Number_of_supplementary_higher_steps = 2

# nothing more to write from there
sorted_step = []

# Automated addition of supplementary steps -> reseach of names for the steps 
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

# Automated addition of supplementary steps -> addition of the steps
for i in range(1, Number_of_supplementary_higher_steps+1):
    if (last_step_type == "A" and i % 2 == 1) or (last_step_type == "B" and i % 2 == 0):
        new_high_step = "B" + str(last_step_height+i)
        sorted_step.append(new_high_step)
    if (last_step_type == "A" and i % 2 == 0) or (last_step_type == "B" and i % 2 == 1):
        new_high_step = "A" + str(last_step_height+i)
        sorted_step.append(new_high_step)

# Add Interface states for cyclic connexions
AllStates = []
for i in range(len(sorted_step)):
    AllStates.append(sorted_step[i])
    AllStates.append(sorted_step[i]+"i")

print AllStates

# Setting parameters of the configuration with previous informations
configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types = AllStates)

# # print tests
# dictionnary_of_possible_types = configuration.possibleTypes()
# print dictionnary_of_possible_types

# list_of_possible_types = dictionnary_of_possible_types.keys()
# del dictionnary_of_possible_types['*']
# print list_of_possible_types
# # end print tests

# Use the _script() function to get a script that can generate the configuration.
print "from KMCLib import *"
print configuration._script()
