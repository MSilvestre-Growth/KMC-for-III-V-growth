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
X = 40
Y = 10
Z = 10

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
types = []

def add_Si_column(column_height, interface="N", Dimere_list=types, max_height=Z):
    if column_height > max_height:
        print "You entered height higher than Z !"
        return 0
    for i in range(max_height):
        if i < column_height:
            if i % 2 == 0:
                if interface == "N":
                    Dimere_list.append("A_Si")
                if interface == "Y":
                    Dimere_list.append("Ai_Si")
            else:
                if interface == "N":
                    Dimere_list.append("B_Si")
                if interface == "Y":
                    Dimere_list.append("Bi_Si")
        else:
            Dimere_list.append("V")
            
def add_Y_row_of_Si_column(column_height, Y_row_length=Y, interface="N", Dimere_list=types, max_height=Z):
    for i in range(Y_row_length):
        add_Si_column(column_height, interface, Dimere_list, max_height)
        

def add_a_Si_steps(step_width, column_height, Y_row_length=Y, interface="N", Dimere_list=types, max_height=Z):
    for i in range(step_width):
        add_Y_row_of_Si_column(column_height, Y_row_length, interface, Dimere_list, max_height)

    
# writting of starting surface

# first step
step_width = X/4
Si_height = 4
add_a_Si_steps(step_width, Si_height)

# second step
step_width = X/4
Si_height = 3
add_a_Si_steps(step_width, Si_height)

# third step
step_width = X/4
Si_height = 2
add_a_Si_steps(step_width, Si_height)

# fourth step
step_width = X/4 - 1
Si_height = 1
add_a_Si_steps(step_width, Si_height)

# fourth step interface
step_width = 1
Si_height = 1
add_a_Si_steps(step_width, Si_height, interface="Y")

# # To distord the final image on plt
# Y_row_length, Y_virtual_row_length = 10, 30


# for i in range(X/4):
#     add_Y_row_of_Si_column(4, Y_row_length)
#     add_Y_row_of_Si_column(0, Y_virtual_row_length)
    
# for i in range(X/4):
#     add_Y_row_of_Si_column(3, Y_row_length)
#     add_Y_row_of_Si_column(0, Y_virtual_row_length)

# for i in range(X/4):
#     add_Y_row_of_Si_column(2, Y_row_length)
#     add_Y_row_of_Si_column(0, Y_virtual_row_length)

# for i in range(X/4):
#     add_Y_row_of_Si_column(1, Y_row_length)
#     add_Y_row_of_Si_column(0, Y_virtual_row_length)

possible_types = ["V", "A_Si", "B_Si", "A_GaAs", "B_GaAs", "Ai_Si", "Bi_Si", "Ai_GaAs", "Bi_GaAs"]


# Setting parameters of the configuration with previous informations
configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types = possible_types)

# Use the _script() function to get a script that can generate the configuration.
print "from KMCLib import *"
print configuration._script()
