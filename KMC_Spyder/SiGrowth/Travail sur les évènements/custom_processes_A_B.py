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

#################################################
#        Deposition of a quasi-dimere           #
#################################################

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

elements_before = ['A', 'B']
elements_after = ['B', 'A']

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
                                           elements_before,
                                           elements_after,
                                           basis_sites=[0],
                                           rate_constant=1.0))

# Create the interactions object.
interactions = KMCInteractions(processes, implicit_wildcards=True)
