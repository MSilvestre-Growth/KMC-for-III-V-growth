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
X = 3
Y = 3
Z = 3

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
types = ["V"] * 13
types.append("Si")
for i in range(13):
    types.append("V")

possible_types = ["Si", "V"]


# Setting parameters of the configuration with previous informations
configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types = possible_types)

# Use the _script() function to get a script that can generate the configuration.
print "from KMCLib import *"
print configuration._script()
