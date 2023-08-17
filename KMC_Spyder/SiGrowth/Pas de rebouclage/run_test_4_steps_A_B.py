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
        
    	 # Physical value
	T = 850 #temperature
    	kb = 1.38*10**(-23)
    	q = 1.6*10**(-19)
    	E_substrate = 1.3
    	E_normal = 0.05
    	E_parallel = 0.5
    	k0 = 10**13
    
    	SendFlux = 0.37

        n_parallel = 0
        n_normal = 0        

    	#print element_before[0]    
        concerned_dimere = elements_before[0]
        dimere_type = concerned_dimere[0]
        
        # Processe's order = [add dimere, go right, go left, go forward, go backward]
        # Repeat X times where X is the number of different steps
        
        #to avoid vacancies diffusion in an higher step
        is_in_bulk = 0
        in_the_last_step = 0
        for i in range(1, 4+1):
            if (int(elements_before[0][1]) <= int(elements_before[i][1])):
                is_in_bulk += 1
        
        # Add a dimere on top case
        if process_number % 9 == 0:
            if is_in_bulk == 4:
                return SendFlux
            else:
                return 0
        
        if is_in_bulk >= 3 and (process_number % 9 != 0):
            return 0
        
        # if process_number % 5 != 0:
        #     return 0
  
        else:
            Move_A = (process_number % 9 != 0) and (dimere_type == 'A')
            Move_B = (process_number % 9 != 0) and (dimere_type == 'B')
        
            ##############################################
            # Jump step event only where there is a step #
            ##############################################
            for i in range(4):
                if (process_number % 9 == 5+i) and int(elements_before[i+1][1]) - int(elements_before[0][1]) != 2:
                    return 0
            
            ###################################
            # Anisotropy is implemented here !#
            ###################################
           
            if Move_A:
               
                if concerned_dimere == elements_before[2]:
                    n_parallel += 1
                if concerned_dimere == elements_before[3]:
                    n_parallel += 1
                if concerned_dimere == elements_before[1]:
                    n_normal += 1
                if concerned_dimere == elements_before[4]:
                    n_normal += 1
               
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                return k0*np.exp( - E_tot * q / (kb * T) )

            
            if Move_B:
                
                if concerned_dimere == elements_before[2]:
                    n_normal +=1
                if concerned_dimere == elements_before[3]:
                    n_normal +=1
                if concerned_dimere == elements_before[1]:
                    n_parallel += 1
                if concerned_dimere == elements_before[4]:
                    n_parallel += 1
                
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                return k0*np.exp( - E_tot * q / (kb * T) )
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0

# Load initial configuration
config = KMCConfigurationFromScript("config_4_steps.py")
#creation of the interaction oject
interactions = KMCInteractionsFromScript("custom_processes_An_Bn_bon_niveaux.py")    
#setting of the CustomRateCalculator in the interaction object
interactions.setRateCalculator(rate_calculator=CustomRateCalculator)


# Generate the KMC model to run.
model = KMCLatticeModel(configuration=config,
                         interactions=interactions)


#Setup the control parameters, note that not specifting
# a seed value will result in the wall clock time seeding,
# so we would expect slightly different results each time
# we run this test.
control_parameters = KMCControlParameters(number_of_steps=1000000,
                                          dump_interval=100000,
                                          seed=120)

model.run(control_parameters, trajectory_filename="custom_traj_4_steps.py")
