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

# ref : Misorientation dependence of epitaxial growth on vicinal GaAs(001)
# DOI : 10.1103/PhysRevB.46.6825
E_substrate = 1.58
E_normal = 0.079
E_parallel = 0.158

# ref : Nucleation and growth of GaAs on Ge and the structure of antiphase boundaries
# DOI : 10.1116/1.583529
E_wrong_bond = 0.3

k0 = 10**13 #hopping constant for the Boltzman's law

SendFlux = 0

print "T°C = ", T
print "SendFlux = ", SendFlux
print "E_normal = ", E_normal
print "E_parallel = ", E_parallel
print "E_wrong_bond = ", E_wrong_bond

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
        
        concerned_element = elements_before[0]
        Xm1 = elements_before[1]
        Xp1 = elements_before[6]
        Ym1 = elements_before[2]
        Yp1 = elements_before[5]
        Zm1 = elements_before[3]
        Zp1 = elements_before[4]
                
        # Events definition
        event_arrival = 0 <= process_number <= 3
        event_GaAs_diffusion = 4 <= process_number <= 83
        
        
        if event_arrival:
            return SendFlux
        
        if event_GaAs_diffusion:
            
            n_parallel = 0
            n_normal = 0
            n_wrong_bond = 0
            
            if elements_before[0] == "A":
                # Xm1
                if Xm1 == "A_GaAs":
                   n_normal += 1
                if Xm1 == "B_GaAs":
                    n_wrong_bond += 1
                if Xm1 == "V":
                    pass
                
                # Xp1
                if Xp1 == "A_GaAs":
                   n_normal += 1
                if Xp1 == "B_GaAs":
                    n_wrong_bond += 1
                if Xp1 == "V":
                    pass
                
                # Ym1
                if Ym1 == "A_GaAs":
                   n_parallel += 1
                if Ym1 == "B_GaAs":
                    n_wrong_bond += 1
                if Ym1 == "V":
                    pass
                
                # Yp1
                if Yp1 == "A_GaAs":
                   n_parallel += 1
                if Yp1 == "B_GaAs":
                    n_wrong_bond += 1
                if Yp1 == "V":
                    pass
                
                # Zm1
                if Zm1 == "A_GaAs":
                    pass
                if Zm1 == "B_GaAs":
                    n_wrong_bond += 1
                
                # Mettre energie de liaison différente avec le substrat ?
                if Zm1 == "A_Si":
                    pass
                
            if elements_before[0] == "B":
                # Xm1
                if Xm1 == "A_GaAs":
                   n_wrong_bond += 1
                if Xm1 == "B_GaAs":
                    n_parallel += 1
                if Xm1 == "V":
                    pass
                
                # Xp1
                if Xp1 == "A_GaAs":
                   n_wrong_bond += 1
                if Xp1 == "B_GaAs":
                    n_parallel += 1
                if Xp1 == "V":
                    pass
                
                # Ym1
                if Ym1 == "A_GaAs":
                   n_wrong_bond += 1
                if Ym1 == "B_GaAs":
                    n_normal += 1
                if Ym1 == "V":
                    pass
                
                # Yp1
                if Yp1 == "A_GaAs":
                   n_wrong_bond += 1
                if Yp1 == "B_GaAs":
                    n_normal += 1
                if Yp1 == "V":
                    pass
                
                # Zm1
                if Zm1 == "A_GaAs":
                    n_wrong_bond
                if Zm1 == "B_GaAs":
                    pass
                
                # Mettre energie de liaison différente avec le substrat ?
                if Zm1 == "B_Si":
                    pass
            
            E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel + n_wrong_bond * E_wrong_bond
            
            return k0*np.exp( - E_tot * q / (kb * T) )
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0 

# speedup process
def TrueFuction(obj):
    return True
CustomRateCalculator.cacheRates = TrueFuction

# Load initial configuration
config = KMCConfigurationFromScript("config_Si2D_for_GaAs3D.py")
#creation of the interaction oject
interactions = KMCInteractionsFromScript("custom_processes_Si2D_for_GaAs3D.py")    
#setting of the CustomRateCalculator in the interaction object
interactions.setRateCalculator(rate_calculator=CustomRateCalculator)

# Generate the KMC model to run.
model = KMCLatticeModel(configuration=config,
                         interactions=interactions)

#Setup the control parameters, note that not specifting
# a seed value will result in the wall clock time seeding,
# so we would expect slightly different results each time
# we run this test.

number_of_steps=1000000

control_parameters = KMCControlParameters(number_of_steps=number_of_steps,
                                          dump_interval=100000,
                                          seed=596312)
name = "trajectory_test.py"
model.run(control_parameters, trajectory_filename=name)
