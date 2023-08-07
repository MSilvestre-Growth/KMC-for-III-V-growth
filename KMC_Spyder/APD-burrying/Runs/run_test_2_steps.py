# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:18:14 2023

@author: msilvestre

"""
from KMCLib import *

#set the custom rate
class CustomRateCalculator(KMCRateCalculatorPlugin):
    """ Class for defining the custom rates function for the KMCLib paper. """

    def rate(self, geometry, elements_before, elements_after, rate_constant, process_number, coordinate):
        """ Overloaded base class API function """
        
        if elements_before[1] == 'A1':
            return 1.0
        else:
            return 0.0

    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0
    

#load initial configuration
config = KMCConfigurationFromScript("config_2_steps.py")

#creation of the interaction oject
interactions = KMCInteractionsFromScript("custom_processes.py")
#setting of the CustomRateCalculator in the interaction object
interactions.setRateCalculator(rate_calculator=CustomRateCalculator)


# Generate the KMC model to run.
model = KMCLatticeModel(configuration=config,
                        interactions=interactions)


# Setup the control parameters, note that not specifting
# a seed value will result in the wall clock time seeding,
# so we would expect slightly different results each time
# we run this test.
control_parameters = KMCControlParameters(number_of_steps=100,
                                          dump_interval=10,
                                          seed=12)

model.run(control_parameters, trajectory_filename="custom_traj_2_steps.py")
