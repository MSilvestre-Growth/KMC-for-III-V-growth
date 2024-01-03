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
X = 100
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
types = ['A19i_Si']*250

for h in range(5250) :
    types.append('A19_Si')
for i in range (6250) :
    types.append('B20_Si')
for j in range(6250) :
    types.append('A21_Si')
for k in range(6250) :
    types.append('B22_Si')
for l in range(750) :
    types.append('A23_Si')

# write all possibles types that you entered previously
possible_types_Si_surface = ['A19i_Si','A19_Si','B20_Si','A21_Si','B22_Si','A23_Si']

# We want to define supplementary steps to be coherent with our step notation
# and atomic processes describes in custom process
Number_of_possible_GaAs_steps = 100

# nothing more to write from there
sorted_step = []

# WARNING : A domains are odd numbers and B domains are even numbers by convention
# Automated addition of supplementary steps -> addition of the steps
for i in range(Number_of_possible_GaAs_steps):
    if i < 10 :
        prefixe = "0"
    else :
        prefixe = ""
    A_step_GaAs = "A" + prefixe + str(i) + "_GaAs"
    sorted_step.append(A_step_GaAs)
    
    A_step_i_GaAs = "A" + prefixe + str(i) + "i_GaAs"
    sorted_step.append(A_step_i_GaAs)
    
    B_step_GaAs = "B" + prefixe + str(i) + "_GaAs"
    sorted_step.append(B_step_GaAs)
    
    B_step_i_GaAs = "B" + prefixe + str(i) + "i_GaAs"
    sorted_step.append(B_step_i_GaAs)

# AllStates = starting Si surface states + GaAs states
AllStates = possible_types_Si_surface

for i in range(len(sorted_step)):
    AllStates.append(sorted_step[i])

print(AllStates)
# print AllStates

# Setting parameters of the configuration with previous informations
configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types = AllStates)

# Use the _script() function to get a script that can generate the configuration.
print "from KMCLib import *"
print configuration._script()
