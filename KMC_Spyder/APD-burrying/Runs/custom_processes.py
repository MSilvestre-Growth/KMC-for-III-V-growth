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

coordinates = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]

# A1 step advance
process_0 = KMCProcess(coordinates=coordinates,
                       elements_before=['B1'],
                       elements_after=['A1'],
                       basis_sites=[0],
                       rate_constant=1.0)

# Create the interactions object.
interactions = KMCInteractions(processes=[process_0, process_1],
                               implicit_wildcards=True)