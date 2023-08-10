# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:18:14 2023

@author: msilvestre

"""
from KMCLib import *

# Set the custom rate --> all the physics is here !!!
class CustomRateCalculator(KMCRateCalculatorPlugin):
    """ Class for defining the custom rates function for the KMCLib paper. """
    
    # Physical values
    Temperature = 850
    kb = 1.38*10**(-23)
    
    E_substrate = 1.3
    E_normal = 0.5
    E_parallel = 0.05
    k0 = 10**13
    
    SendFlux = 0.1
    
    def rate(self, geometry, elements_before, elements_after, rate_constant, process_number, coordinate):
        """ Overloaded base class API function """
        
        concerned_dimere = element_before[0]
        dimere_type = concerned_dimere[0]
        dimere_height = int(concerned_dimere[1])
        
        # Add a dimere on top case
        if process_number == dimere_height:
            return SendFlux + k0*exp(-(E_substrate+E_normal+E_parallel)/(kb * T))
        
        # Remove the dimere case
        if process_number == dimere_height + 1:
            return k0*exp(-(E_substrate+E_normal+E_parallel)/(kb * T))
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0

# Load initial configuration
config = KMCConfigurationFromScript("config_3_steps.py")
#creation of the interaction oject
interactions = KMCInteractionsFromScript("custom_processes.py")    
# #setting of the CustomRateCalculator in the interaction object
# interactions.setRateCalculator(rate_calculator=CustomRateCalculator)


# # Generate the KMC model to run.
# model = KMCLatticeModel(configuration=config,
#                         interactions=interactions)


# # Setup the control parameters, note that not specifting
# # a seed value will result in the wall clock time seeding,
# # so we would expect slightly different results each time
# # we run this test.
# control_parameters = KMCControlParameters(number_of_steps=100,
#                                           dump_interval=10,
#                                           seed=12)

# model.run(control_parameters, trajectory_filename="custom_traj_2_steps.py")
