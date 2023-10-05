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

processes.append(KMCProcess(coordinates=coordinates,
                                       elements_before=["0"],
                                       elements_after=["1"],
 

# Create the interactions object with previous parameters.
interactions = KMCInteractions(processes, implicit_wildcards=True)
