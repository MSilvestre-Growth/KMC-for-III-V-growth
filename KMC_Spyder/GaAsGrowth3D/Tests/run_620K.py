# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:18:14 2023

@author: msilvestre

This is where you implement physics. The rate function in the CustomRateCalculator
allows you to set probabilities of each events defined in custom_processes.py
- In first time you set physical constants such as energies, atomic flux and
temperature.
- In a second time, you take neigbors into acount, which affect event's 
probabilities and allows you to avoid some events when the local configuration 
does not allow them.
- In a third time, you explicitly write the event probability (most often it is
based on Boltzman's law)
- The last thing you need to set up is the number of simulation steps and how
often you save a configuration in custom_traj.py

WARNING : the highest step is considered to be the highest on the wafer,
there is no stepflow above it
"""
from KMCLib import *
import numpy as np
import time
#from KMCLib.KMCAnalysisPlugin import KMCAnalysisPlugin

# Physical value
T = 620 #temperature
kb = 1.38*10**(-23)
q = 1.6*10**(-19)
E_substrate = 1.3
E_normal = 0.05
E_parallel = 0.5
k0 = 10**13 #hopping constant for the Boltzman's law

SendFlux = 1

print "T°C = ", T
print "SendFlux = ", SendFlux
print "E_normal = ", E_normal
print "E_parallel = ", E_parallel

# Set the custom rate --> all the physics is here !!!
class CustomRateCalculator(KMCRateCalculatorPlugin):
    """ Class for defining the custom rates function for the KMCLib paper. """
    
    
    def rate(self, geometry, elements_before, elements_after, rate_constant, process_number, coordinate):
        """ Overloaded base class API function """
        #print process_number
        
        # Physical value
        global T
        global kb
        global q
        global E_substrate
        global E_normal
        global E_parallel
        global k0

        global SendFlux
        
        if 0<=process_number<=7 and process_number != 0:
            return 0.0
        else:
            return 1.0
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0 

# speedup process
def TrueFuction(obj):
    return True
CustomRateCalculator.cacheRates = TrueFuction

# Load initial configuration
config = KMCConfigurationFromScript("config3D.py")
#creation of the interaction oject
interactions = KMCInteractionsFromScript("custom_processes_bis.py")    
#setting of the CustomRateCalculator in the interaction object
interactions.setRateCalculator(rate_calculator=CustomRateCalculator)

# Generate the KMC model to run.
model = KMCLatticeModel(configuration=config,
                         interactions=interactions)

#Setup the control parameters, note that not specifting
# a seed value will result in the wall clock time seeding,
# so we would expect slightly different results each time
# we run this test.

number_of_steps=10

control_parameters = KMCControlParameters(number_of_steps=number_of_steps,
                                          dump_interval=1,
                                          seed=596312)
name = "trajectory_test.py"
model.run(control_parameters, trajectory_filename=name)
