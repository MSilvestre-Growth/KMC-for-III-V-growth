# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:18:14 2023

@author: msilvestre

"""
from KMCLib import *
import numpy as np
# Set the custom rate --> all the physics is here !!!
class CustomRateCalculator(KMCRateCalculatorPlugin):
    """ Class for defining the custom rates function for the KMCLib paper. """
    
    
    def rate(self, geometry, elements_before, elements_after, rate_constant, process_number, coordinate):
        """ Overloaded base class API function """
        
    	# Physical values
    	T = 850#temperature
    	kb = 1.38*10**(-23)
    	q = 1.6*10**(-19)
    	E_substrate = 1.3
    	E_normal = 0.5
    	E_parallel = 0.05
    	k0 = 10**13
    
    	SendFlux = 100

        n_parallel = 0
        n_normal = 0        

    	#print element_before[0]    
        concerned_dimere = elements_before[0]
        dimere_type = concerned_dimere[0]
        dimere_height = int(concerned_dimere[1])
        
        for i in range(1, 4+1):
            if dimere_type == elements_before[i][0]:
                n_parallel += 1
            else:
                n_normal +=1
        # Add a dimere on top case
        if process_number == 2*(dimere_height - 1):
            return SendFlux + k0*np.exp(-(E_substrate+E_normal+E_parallel)*q/(kb * T))
        
        # Remove the dimere case
        if process_number == 2*(dimere_height-1)+1:
            return k0*np.exp(-(E_substrate+E_normal+E_parallel)*q/(kb * T))
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0

# Load initial configuration
config = KMCConfigurationFromScript("config_4_steps.py")
#creation of the interaction oject
interactions = KMCInteractionsFromScript("custom_processes.py")    
#setting of the CustomRateCalculator in the interaction object
interactions.setRateCalculator(rate_calculator=CustomRateCalculator)


# Generate the KMC model to run.
model = KMCLatticeModel(configuration=config,
                         interactions=interactions)


#Setup the control parameters, note that not specifting
# a seed value will result in the wall clock time seeding,
# so we would expect slightly different results each time
# we run this test.
control_parameters = KMCControlParameters(number_of_steps=1000,
                                          dump_interval=100,
                                          seed=120)

model.run(control_parameters, trajectory_filename="custom_traj_4_steps.py")
