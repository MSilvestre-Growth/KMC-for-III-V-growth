# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:18:14 2023

@author: msilvestre

"""
from KMCLib import *

configuration = KMCConfigurationFromScript("config.py")
interactions  = KMCInteractionsFromScript("custom_processes.py")

# Generate the KMC model to run.
model = KMCLatticeModel(configuration=config,
                        interactions=interactions)

# Setup the control parameters, note that not specifting
# a seed value will result in the wall clock time seeding,
# so we would expect slightly different results each time
# we run this test.
control_parameters = KMCControlParameters(number_of_steps=2500000,
                                          dump_interval=10000,
                                          analysis_interval=100,
                                          seed=12)

model.run(control_parameters, trajectory_filename="custom_traj.py")