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


# Set the custom rate --> all the physics is here !!!
class CustomRateCalculator(KMCRateCalculatorPlugin):
    """ Class for defining the custom rates function for the KMCLib paper. """
    
    
    def rate(self, geometry, elements_before, elements_after, rate_constant, process_number, coordinate):
        """ Overloaded base class API function """
        #print process_number

        # Physical value
        T = 850 #temperature
        kb = 1.38*10**(-23)
        q = 1.6*10**(-19)
        E_substrate = 1.3
        E_normal = 0.05
        E_parallel = 0.5
        k0 = 10**13 #hopping constant for the Boltzman's law
    
        SendFlux = 0.16666667 

        n_parallel = 0
        n_normal = 0

        Nb_processes_per_type = 20
    

    	#print element_before[0]    
        concerned_dimere = elements_before[0]
        dimere_type = concerned_dimere[0]
        
        # Processe's order = [add dimere, go right, go left, go forward, go backward,
        # jump forward, jump left, jump right, jump backward]
        # Repeat X times where X is the number of different steps
        
        ############################
        #    Is in bulk section    #
        ############################
        
        #to avoid vacancies diffusion in an higher step
        is_in_bulk = 0
        for i in range(1, 4+1):
            if (int(elements_before[0][1]) <= int(elements_before[i][1])) and (len(concerned_dimere) == 2) :	
                is_in_bulk += 1
        
        # Interface dimeres are not in bulk to be coherent with others processes
        if len(concerned_dimere) == 3 :
            is_in_bulk = 0
        
        ##############################
        #    Add a dimere section    #
        ##############################
        
        # Add a dimere on top case
        if process_number % Nb_processes_per_type == 0 or process_number % Nb_processes_per_type == 1 :
            return SendFlux
        
        ###########################
        #    Diffusion section    #
        ###########################
        diffusion = process_number % Nb_processes_per_type >= 2 and process_number % Nb_processes_per_type <= 5
        diffusion_interface= process_number % Nb_processes_per_type >= 10 and process_number % Nb_processes_per_type <= 13
        diffusion_for_cycling = process_number % Nb_processes_per_type == 18 or process_number % Nb_processes_per_type == 19
        
        if diffusion_for_cycling and int(concerned_dimere[1]) >= 6 :
            return 0
        
        all_diffusion = diffusion or diffusion_interface or diffusion_for_cycling
        
        if is_in_bulk >= 3 and all_diffusion :
            return 0
        
        if is_in_bulk < 3 and all_diffusion :
            #print process_number
            #print concerned_dimere 
            Move_A = (dimere_type == 'A')
            Move_B = (dimere_type == 'B')
       
            ###################################
            # Anisotropy is implemented here !#
            ###################################
           
            if Move_A:
               
                if concerned_dimere[1] <= elements_before[1][1]:
                    n_normal += 1
                if concerned_dimere[1] <= elements_before[2][1]:
                    n_parallel += 1
                if concerned_dimere[1] <= elements_before[3][1]:
                    n_parallel += 1
                if (concerned_dimere[1] <= elements_before[4][1]) or (
                        (elements_before[4] == "B" + str(int(elements_before[0][1])-3)+"i")):
                    n_normal += 1
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                return k0*np.exp( - E_tot * q / (kb * T) )

            
            if Move_B:
                if concerned_dimere[1] <= elements_before[1][1]:
                    n_parallel += 1
                if concerned_dimere[1] <= elements_before[2][1]:
                    n_normal +=1
                if concerned_dimere[1] <= elements_before[3][1]:
                    n_normal +=1
                if (concerned_dimere[1] <= elements_before[4][1]) or (
                        (elements_before[4] == "A" + str(int(elements_before[0][1])-3)+"i")):
                    n_parallel += 1
                
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                return k0*np.exp( - E_tot * q / (kb * T) )
            
        #########################
        #    Jumping section    #
        #########################
        
        jump = process_number % Nb_processes_per_type >= 6 and process_number % Nb_processes_per_type <= 9
        jump_interface= process_number % Nb_processes_per_type >= 14 and process_number % Nb_processes_per_type <= 17
        all_jump = jump or jump_interface
        
        is_alone = 0
        
        for i in range(1,4+1):
            if (int(elements_before[0][1]) == (int(elements_before[i][1])+1)) :	
                is_alone += 1
        
        if is_alone == 4 and all_jump :
            return k0
        
        if is_alone != 4 and all_jump :
            return 0
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0

# speedup process
def TrueFuction(obj):
    return True

CustomRateCalculator.cacheRates = TrueFuction

# Load initial configuration
config = KMCConfigurationFromScript("config_3_steps.py")
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
control_parameters = KMCControlParameters(number_of_steps=10000000,
                                          dump_interval=1000000,
                                          seed=596312)
t1 = time.clock()
model.run(control_parameters, trajectory_filename="custom_traj_3_steps.py")
t2 = time.clock()

print "simu time = "
print t2 - t1



