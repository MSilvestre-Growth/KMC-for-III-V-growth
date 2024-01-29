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
T = 673 #temperature
kb = 1.38*10**(-23)
q = 1.6*10**(-19)

# ref : Misorientation dependence of epitaxial growth on vicinal GaAs(001)
# DOI : 10.1103/PhysRevB.46.6825
E_GaAs = 1.3
E_normal = 0.3
E_parallel = 0.15

E_Si = 1.1

k0 = 10**13 #hopping constant for the Boltzman's law

SendFlux = 0.6

# ref : Nucleation and growth of GaAs on Ge and the structure of antiphase boundaries
# DOI : 10.1116/1.583529
E_wrong_bond = 0.3 # 0.3

# ref : Influence of Schwoebel barrier and diffusion anisotropy on step density oscillation amplitude during epitaxial growth
# DOI : 10.1016/j.commatsci.2005.03.020

E_sc = 0 # 2.3*kb*T/q

# ref : Anisotropy in surface migration of Si and Ge on Si(OO1)
# DOI : 10.1016/0039-6028(91)91177-Y
k_parallel_Si = 1
k_normal_Si = 1000

# ref : ANISOTROPIC SURFACE MIGRATION OF Ga ATOMS ON GaAs (001)
# DOI : 10.1016/0022-0248(89)90354-0
k_parallel_GaAs = 4
k_normal_GaAs = 1

print "T°C = ", T
print "SendFlux = ", SendFlux
print "E_normal = ", E_normal
print "E_parallel = ", E_parallel
print "E_wrong_bond = ", E_wrong_bond
print "E_Si = ", E_Si
print "E_sc = ", E_sc
print "k_parallel_Si = ", k_parallel_Si
print "k_normal_Si = ", k_normal_Si

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
        global E_GaAs
        global E_normal
        global E_parallel
        global k0

        global SendFlux
	#print process_number
	#print elements_before        
        concerned_element = elements_before[0]
        Xm1 = elements_before[1]
        Xp1 = elements_before[6]
        Ym1 = elements_before[2]
        Yp1 = elements_before[5]
        Zm1 = elements_before[3]
        Zp1 = elements_before[4]
        
        # Events definition
        event_arrival = 0 <= process_number <= 3
        event_GaAs_diffusion = 4 <= process_number <= 98
        
        event_jump_alone = 100 <= process_number <= 115
        
        if event_arrival:
 	    #print "arrival"
            return SendFlux
        
        if event_jump_alone:
            if ((event_jump_alone-100) % 4 == 0) and elements_before[45] == "V":
                return 0
            if ((event_jump_alone-100) % 4 == 1) and elements_before[43] == "V":
                return 0
            if ((event_jump_alone-100) % 4 == 2) and elements_before[50] == "V":
                return 0
            if ((event_jump_alone-100) % 4 == 3) and elements_before[38] == "V":
                return 0
            else:
                return k0
        
        if event_GaAs_diffusion:
            #print elements_before[0][0] 
            n_parallel = 0
            n_normal = 0
            n_wrong_bond = 0
            E_underlayer = 0
            k = k0
            
            n_step_edge = 0
            if 12 <= process_number <= 19:
                n_step_edge = 1
            
            # diffusion anisotropy on Si
            if 4 <= process_number <= 51:
                if (process_number-4 % 4 == 0) or (process_number-4 % 4 == 1):
                    if elements_before[0][0] == "A":
                        k = k * k_parallel_Si
                    if elements_before[0][0] == "B":
                        k = k * k_normal_Si
                        
                if (process_number-4 % 4 == 2) or (process_number-4 % 4 == 3):
                    if elements_before[0][0] == "A":
                        k = k * k_normal_Si
                    if elements_before[0][0] == "B":
                        k = k * k_parallel_Si
            
            
            if elements_before[0][0] == "A":
                # Xm1
                if Xm1 == "A_GaAs":
                    n_normal += 1
                # if Xm1 == "B_GaAs":
                #     n_wrong_bond += 1
                # if Xm1 == "V":
                #     pass
               
                # Xp1
                if Xp1 == "A_GaAs":
                    n_normal += 1
                # if Xp1 == "B_GaAs":
                #     n_wrong_bond += 1
                # if Xp1 == "V":
                #     pass
               
                # Ym1
                if Ym1 == "A_GaAs":
                    n_parallel += 1
                # if Ym1 == "B_GaAs":
                #     n_wrong_bond += 1
                # if Ym1 == "V":
                #     pass
               
                # Yp1
                if Yp1 == "A_GaAs":
                    n_parallel += 1
                # if Yp1 == "B_GaAs":
                #     n_wrong_bond += 1
                # if Yp1 == "V":
                #     pass
               
                # Zm1
                if Zm1 == "A_GaAs":
                    E_underlayer = E_GaAs
                    k = k * k_parallel_GaAs
                if Zm1 == "B_GaAs":
                    n_wrong_bond += 1
                    E_underlayer = E_GaAs
                    k = k * k_normal_GaAs
               
                #Mettre energie de liaison différente avec le substrat ?
                if Zm1 == "A_Si":
                    E_underlayer = E_Si
                if Zm1 == "B_Si":
                    n_wrong_bond += 1
                    E_underlayer = E_Si
               
            if elements_before[0][0] == "B":
                # Xm1
                # if Xm1 == "A_GaAs":
                #     n_wrong_bond += 1
                if Xm1 == "B_GaAs":
                    n_parallel += 1
                # if Xm1 == "V":
                #     pass
               
                # Xp1
                # if Xp1 == "A_GaAs":
                #     n_wrong_bond += 1
                if Xp1 == "B_GaAs":
                    n_parallel += 1
                # if Xp1 == "V":
                #     pass
               
                # Ym1
                # if Ym1 == "A_GaAs":
                #     n_wrong_bond += 1
                if Ym1 == "B_GaAs":
                    n_normal += 1
                # if Ym1 == "V":
                #     pass
               
                # Yp1
                # if Yp1 == "A_GaAs":
                #     n_wrong_bond += 1
                if Yp1 == "B_GaAs":
                    n_normal += 1
                # if Yp1 == "V":
                #     pass
               
                # Zm1
                if Zm1 == "A_GaAs":
                    n_wrong_bond += 1
                    E_underlayer = E_GaAs
                    k = k * k_normal_GaAs
                if Zm1 == "B_GaAs":
                    E_underlayer = E_GaAs
                    k = k * k_parallel_GaAs
               
                #Mettre energie de liaison différente avec le substrat ?
                if Zm1 == "A_Si":
                    n_wrong_bond += 1
                    E_underlayer = E_Si
                if Zm1 == "B_Si":
                    E_underlayer = E_Si
            
            if E_underlayer == 0:
                print process_number
		print elements_before
            E_tot = E_underlayer + n_normal * E_normal + n_parallel * E_parallel + n_wrong_bond * E_wrong_bond + n_step_edge * E_sc
            
            return k*np.exp( - E_tot * q / (kb * T) )
 	else:
 	    return 0
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 2.24

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

number_of_steps = 50000000

control_parameters = KMCControlParameters(number_of_steps=number_of_steps,
                                          dump_interval=500000,
                                          seed=596312)
name = "trajectory_test.py"
model.run(control_parameters, trajectory_filename=name)
