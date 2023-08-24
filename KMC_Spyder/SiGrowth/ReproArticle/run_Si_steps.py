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
        
        # Physical value
        T = 950 #temperature
        kb = 1.38*10**(-23)
        q = 1.6*10**(-19)
        E_substrate = 1.3
        E_normal = 0.05
        E_parallel = 0.5
        k0 = 10**13 #hopping constant for the Boltzman's law
    
        SendFlux =2.34 

        n_parallel = 0
        n_normal = 0

        Nb_processes_per_type = 5        

    

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
        if process_number % Nb_processes_per_type == 0:
            if is_in_bulk == 4:
                
		return SendFlux
            else:
                return 0
        
        if is_in_bulk >= 3 and (process_number % Nb_processes_per_type != 0):
            return 0
  
        else:
            Move_A = (process_number % Nb_processes_per_type != 0) and (dimere_type == 'A')
            Move_B = (process_number % Nb_processes_per_type != 0) and (dimere_type == 'B')
                   
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

#class CustomAnalysis(KMCAnalysisPlugin):
#    """ Custom analysis class """
#    def __init__(self, init_config, current_config):
#        self.init_config = init_config
#        self.curent_config = current_config
	
#    def setup(self, step, time, configuration):
#        if step == 0:
#            fig0 = configuration.types()
#        fig_now = configuration.types()
#        p = CustomAnalysis(config0, config_now)
#        return comp
    
#    def finalize(self):
#        p = setup(step, time, configuration)
#        t_types = comp.init_config()
#        rent_types = comp.current_config()
#        t_atoms = 0
#        i in range(len(init_types)):
#             sent_atoms += int(current_types[i][1]) - int(init_types[i][1])
#        return sent_atoms/(len(init_types)*time)

#analysis = CustomAnalysis.finalize()

# speedup process
def TrueFuction(obj):
    return True

CustomRateCalculator.cacheRates = TrueFuction

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
control_parameters = KMCControlParameters(number_of_steps=1000000,
                                          dump_interval=100000, 
                                          seed=120)
t1 = time.clock()
model.run(control_parameters, trajectory_filename="custom_traj_4_steps.py")
t2 = time.clock()

print "simu time = "
print t2 - t1



