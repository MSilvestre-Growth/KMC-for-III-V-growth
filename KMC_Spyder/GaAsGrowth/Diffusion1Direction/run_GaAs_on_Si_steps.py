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

# store the configuration to get all possibles types
config = KMCConfigurationFromScript("config_4_steps.py")

# Get the possible types from config
dictionnary_of_possible_types = config.possibleTypes()
#print dictionnary_of_possible_types

# Removal of generic '*' type from the dictionnary
del dictionnary_of_possible_types['*']

# Conversion of a dictionnary in the list of all entries
list_of_possible_types = dictionnary_of_possible_types.keys()
    
Nb_possible_overgrowth = len(list_of_possible_types)
    
Nb_sent_atoms = 0
Nb_sent_atoms_previous = 0

# Set the custom rate --> all the physics is here !!!
class CustomRateCalculator(KMCRateCalculatorPlugin):
    """ Class for defining the custom rates function for the KMCLib paper. """
    

    
    def rate(self, geometry, elements_before, elements_after, rate_constant, process_number, coordinate):
        """ Overloaded base class API function """
        
        global Nb_possible_overgrowth
        global Nb_sent_atoms
        global Nb_sent_atoms_previous
        
        # Physical value
        T = 650 #temperature
        kb = 1.38*10**(-23)
        q = 1.6*10**(-19)
        E_substrate = 1.3
        E_normal = 0.05
        E_parallel = 0.5
        k0 = 10**13 #hopping constant for the Boltzman's law
    
        SendFlux =10 

        n_parallel = 0
        n_normal = 0        
        
        Nb_process_per_type = 5 + Nb_possible_overgrowth

    	#print element_before[0]    
        concerned_dimere = elements_before[0]
        dimere_type = concerned_dimere[0]
        
        # Processe's order = [add dimere, go right, go left, go forward, go backward,
        # jump forward, jump left, jump right, jump backward]
        # Repeat X times where X is the number of different steps
        
        #to avoid vacancies diffusion in an higher step
        is_in_bulk = 0
        in_the_last_step = 0
        for i in range(1, 4+1):
            if (int(elements_before[0][1]) <= int(elements_before[i][1])):
                is_in_bulk += 1
        
        # Add a dimere on top case
        if process_number % Nb_process_per_type == 0:
            if is_in_bulk == 4:
                Nb_sent_atoms += 1
                return SendFlux
            # Overgrowth
            if (is_in_bulk < 4) and (process_number % Nb_process_per_type > 4):
                if dimere_type == 'A' and ((abs(int(elements_before[2][1])-int(elements_before[0][1])) == 1) or (abs(int(elements_before[3][1])-int(elements_before[0][1])) == 1)) and (process_number - (process_number % Nb_process_per_type)) / Nb_process_per_type >= int(elements_before[0][1]):
                    print "overGrowth A"
                    Nb_sent_atoms += 1
                    return SendFlux
            
            if (is_in_bulk < 4) and (process_number % Nb_process_per_type > 4):
                if dimere_type == 'B' and ((abs(int(elements_before[1][1])-int(elements_before[0][1])) == 1) or (abs(int(elements_before[4][1])-int(elements_before[0][1])) == 1)) and (process_number - (process_number % Nb_process_per_type)) / Nb_process_per_type >= int(elements_before[0][1]):
                    print "OverGrowth B"
                    Nb_sent_atoms += 1
                    return SendFlux
            else:
                return 0
        
        if is_in_bulk >= 3 and (process_number % Nb_process_per_type != 0):
            return 0
        
        else:
            Move_A = (process_number % Nb_process_per_type != 0) and (dimere_type == 'A')
            Move_B = (process_number % Nb_process_per_type != 0) and (dimere_type == 'B')
        
            ##############################################
            # Jump step event only where there is a step #
            ##############################################
            # for i in range(4):
            #     if (process_number % Nb_process_per_type == 5+i) and int(elements_before[i+1][1]) - int(elements_before[0][1]) != 2:
            #         return 0
            
            ###################################
            # Anisotropy is implemented here !#
            ###################################
           
            if Move_A:
                if (process_number % Nb_process_per_type == 2) or (process_number % Nb_process_per_type == 3):
                    return 0
                else :
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
                if (process_number % Nb_process_per_type == 1) or (process_number % Nb_process_per_type == 4):
                    return 0
                else :                
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
                
        if Nb_sent_atoms_previous < Nb_sent_atoms :
            Nb_sent_atoms_previous = Nb_sent_atoms
            print Nb_sent_atoms
        
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
control_parameters = KMCControlParameters(number_of_steps=10000,
                                          dump_interval=1000,
                                          seed=120)

model.run(control_parameters, trajectory_filename="custom_traj_GaAs_on_Si_4_steps.py")
