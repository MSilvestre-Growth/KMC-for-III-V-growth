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
T = 950 #temperature
kb = 1.38*10**(-23)
q = 1.6*10**(-19)
E_substrate = 1.3
E_normal = 0.05
E_parallel = 0.5
k0 = 10**13 #hopping constant for the Boltzman's law

SendFlux = 2 

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
        
        # Utilities for the custom rate
        #if process_number<=55:
        #    return 0
        Nb_processes_per_type =30
        
        Number_of_step_on_starting_surface = 4
        
        if Number_of_step_on_starting_surface % 2 == 1 :
            Cycling_letter_moving_A = "B"
            Cycling_letter_moving_B = "A"
            
        else :
            Cycling_letter_moving_A = "A"
            Cycling_letter_moving_B = "B"
       
        concerned_dimere = elements_before[0]
        dimere_type = concerned_dimere[0]
        
        # PLEASE DON'T TOUCH THIS: this is the list of the 1st nearest neighbourg
        # of the nearest neigbourg up to rank 4 (this iis linked with the cutoff value = 3.17)
        # list_of_neighbourg_of_neighbourg = [[0, 1, 2, 3, 4],
        #                                     [1, 9, 5, 6, 0],
        #                                     [2, 5, 10, 0, 7],
        #                                     [3, 6, 0, 11, 8],
        #                                     [4, 0, 7, 8, 12],
        #                                     [5, 13, 15, 1, 2],
        #                                     [6, 14, 1, 16, 3],
        #                                     [7, 2, 17, 4, 19],
        #                                     [8, 3, 4, 18, 20],
        #                                     [9, 25, 13, 14, 1],
        #                                     [10, 15, 26, 2, 17],
        #                                     [11, 16, 3, 27, 18],
        #                                     [12, 4, 19, 20, 28],
        #                                     [13, 29, 21, 9, 5],
        #                                     [14, 30, 9, 22, 6],
        #                                     [15, 21, 31, 5, 10],
        #                                     [16, 22, 6, 32, 11],
        #                                     [17, 10, 33, 7, 23],
        #                                     [18, 11, 8, 34, 24],
        #                                     [19, 7, 23, 12, 35],
        #                                     [20, 8, 12, 24, 36]]
        
        # Processe's order = [add dimere, go right, go left, go forward, go backward,
        # jump forward, jump left, jump right, jump backward]
        # Repeat X times where X is the number of different steps
        
        ############################
        #    Is in bulk section    #
        ############################
        
        #to avoid vacancies diffusion in an higher step
        # is_in_bulk = 0
        # for i in range(1, 4+1):
        #     if int(elements_before[0][1:3]) <= int(elements_before[i][1:3]):	
        #         a = 1
        #         # ex: if A05 is top and A01i is bottom, A05 is_in_bulk + 1
        #         # but if B06 is top and A01i is bottom, B06 is_in_bulk + 0 (thanks to the following line)
        #         if (i == 4) and (len(elements_before[4]) == 4) and (int(elements_before[4][1:3]<int(concerned_dimere[1:3])-4)):
        #             a = 0
        #         # ex : if B22 is top and B20i is bottom, B20i is_in_bulk + 0
        #         if (i == 1) and (len(concerned_dimere) == 4) and (int(elements_before[1][1:3])<int(concerned_dimere[1:3])+4):
        #             a = 0
        #         is_in_bulk += a
                
        # # ex: if A05 is top and A01i is bottom, A01i is_in_bulk + 1
        # if (len(concerned_dimere) == 4) and (int(elements_before[1][1:3]>=int(concerned_dimere[1:3])+4)):
        #     is_in_bulk += 1
        
        is_in_bulk = 0
        for i in range(1, 4+1):
            if (i == 2) or (i == 3) :
                if int(concerned_dimere[1:3]) <= int(elements_before[i][1:3]):	
                    is_in_bulk += 1
            
            if i == 1:
                if len(concerned_dimere) == 3:
                    if int(concerned_dimere[1:3]) <= int(elements_before[1][1:3]):	
                        is_in_bulk += 1
                if len(concerned_dimere) == 4:
                    if int(elements_before[1][1:3])>=int(concerned_dimere[1:3])+4:
                        is_in_bulk += 1
            
            if i == 4:
                if len(elements_before[4]) == 3:
                    if int(concerned_dimere[1:3]) <= int(elements_before[4][1:3]):	
                        is_in_bulk += 1
                if len(elements_before[4]) == 4:
                    if int(elements_before[4][1:3])>=int(concerned_dimere[1:3])-4:
                        is_in_bulk += 1
        
        if concerned_dimere == "A21i":
            print "is_in_bulk ", is_in_bulk
        
        ##############################
        #    Add a dimere section    #
        ##############################
        
        # Add a dimere on top case
        if process_number % Nb_processes_per_type == 0 or process_number % Nb_processes_per_type == 1 :
            # # Calculation of coordinance of each nearest neighbourg :
            # list_of_coordinance_4 = []
            # list_of_coordinance_3 = []
            # list_of_coordinance_2 = []
            # list_of_coordinance_1 = []
            # list_of_coordinance_0 = []
            
            # coordinance_of_current_element = 0
            
            # for i in range(len(list_of_neighbourg_of_neighbourg)):
            #     coordinance = 0
            #     for j in range(4):
            #         if list_of_neighbourg_of_neighbourg[i][j+1] > list_of_neighbourg_of_neighbourg[i][0]:
            #             coordinance += 1
                        
            #     if i == 0:
            #         coordinance_of_current_element = coordinance
            
            #     if coordinance == 0:
            #         list_of_coordinance_0.append(list_of_neighbourg_of_neighbourg[i][0])
            #     if coordinance == 1:
            #         list_of_coordinance_1.append(list_of_neighbourg_of_neighbourg[i][0])
            #     if coordinance == 2:
            #         list_of_coordinance_2.append(list_of_neighbourg_of_neighbourg[i][0])
            #     if coordinance == 3:
            #         list_of_coordinance_3.append(list_of_neighbourg_of_neighbourg[i][0])
            #     if coordinance == 4:
            #         list_of_coordinance_4.append(list_of_neighbourg_of_neighbourg[i][0])
            
            # if coordinance_of_current_element == 4:
            #     return 15 * SendFlux / len(list_of_coordinance_4)
            
            # if coordinance_of_current_element == 3 and len(list_of_coordinance_4) == 0:
            #     return 15 * SendFlux / len(list_of_coordinance_3)
            
            # if coordinance_of_current_element == 2 and len(list_of_coordinance_4) == 0 and len(list_of_coordinance_3) == 0:
            #     return 15 * SendFlux / len(list_of_coordinance_2)
        
            # if coordinance_of_current_element == 1 and len(list_of_coordinance_4) == 0 and len(list_of_coordinance_3) == 0 and len(list_of_coordinance_2) == 0:
            #     return 15 * SendFlux / len(list_of_coordinance_1)
            
            # if coordinance_of_current_element == 0 and len(list_of_coordinance_4) == 0 and len(list_of_coordinance_3) == 0 and len(list_of_coordinance_2) == 0 and len(list_of_coordinance_1) == 0:
            #     return 15 * SendFlux / len(list_of_coordinance_0)

            # else:
            #     return 0
            return SendFlux
	
        ###########################################
        #    Jumping down from a single dimere    #
        ###########################################
        
        if  process_number % Nb_processes_per_type == 6 or  process_number % Nb_processes_per_type == 7 or  process_number % Nb_processes_per_type == 8 or  process_number % Nb_processes_per_type == 9 process_number % Nb_processes_per_type == 28 or  process_number % Nb_processes_per_type == 29:
            is_alone = 0
            for i in range(4):
                if int(concerned_dimere[1:3]) == int(elements_before[i+1][1:3]) + 1:
                    is_alone +=1
                if is_alone == 4:
                    return k0
           
        ###########################
        #    Diffusion section    #
        ###########################
        diffusion = process_number % Nb_processes_per_type >= 2 and process_number % Nb_processes_per_type <= 5
        jump = process_number % Nb_processes_per_type >= 6 and process_number % Nb_processes_per_type <= 13
        diffusion_interface= process_number % Nb_processes_per_type >= 14 and process_number % Nb_processes_per_type <= 17
        jump_interface = process_number % Nb_processes_per_type >= 18 and process_number % Nb_processes_per_type <= 25
        diffusion_for_cycling = process_number % Nb_processes_per_type == 26 or process_number % Nb_processes_per_type == 27
        
        # if diffusion_for_cycling and int(concerned_dimere[1]) >= 6 :
        #     return 0
        
        normal_diffusion = diffusion or diffusion_interface or jump or jump_interface
        all_diffusion = normal_diffusion or diffusion_for_cycling
        
        # Avoid B8 apparition on A1 step
        # max_height = 9
        # if (int(elements_before[0][1:3]) > max_height - 4) and (diffusion_for_cycling or jump or jump_interface):
        #     return 0
        
        if is_in_bulk >= 4 and all_diffusion :
            return 0
        
        if is_in_bulk < 4 and normal_diffusion :
            
            n_parallel = 0
            n_normal = 0
            
            #print process_number
            #print concerned_dimere 
            Move_A = (dimere_type == 'A')
            Move_B = (dimere_type == 'B')
       
            ###################################
            # Anisotropy is implemented here !#
            ###################################
           
            if Move_A:
                if elements_before[1] == Cycling_letter_moving_B + str(int(elements_before[0][1:3])+Number_of_step_on_starting_surface-1):
                    #print concerned_dimere
                    #print Cycling_letter_moving_B + str(int(elements_before[0][1:3])+Number_of_step_on_starting_surface-1)
                    n_normal += 0
                else:
                    if int(concerned_dimere[1:3]) <= int(elements_before[1][1:3]):
                        n_normal += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[2][1:3]):
                    n_parallel += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[3][1:3]):
                    n_parallel += 1
                if elements_before[4] == Cycling_letter_moving_B + str(int(elements_before[0][1:3])-Number_of_step_on_starting_surface-1)+"i":
                    #print concerned_dimere
                    #print Cycling_letter_moving_B + str(int(elements_before[0][1:3])-Number_of_step_on_starting_surface-1)+"i"
                    n_normal +=0
                else:
                    if int(concerned_dimere[1:3]) <= int(elements_before[4][1:3]):                       		    n_normal += 1
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                if concerned_dimere == "A21i":
                    print "Etot moving", E_tot
                return k0*np.exp( - E_tot * q / (kb * T) )
            
            if Move_B:
                if elements_before[1] == Cycling_letter_moving_A + str(int(elements_before[0][1:3])+Number_of_step_on_starting_surface-1):
                    #print concerned_dimere
                    #print Cycling_letter_moving_A + str(int(elements_before[0][1:3])+Number_of_step_on_starting_surface-1)
                    n_parallel += 0
                else:
                    if int(concerned_dimere[1:3]) <= int(elements_before[1][1:3]):
                        n_parallel += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[2][1:3]):
                    n_normal +=1
                if int(concerned_dimere[1:3]) <= int(elements_before[3][1:3]):
                    n_normal +=1
                if elements_before[4] == Cycling_letter_moving_A + str(int(elements_before[0][1:3])-Number_of_step_on_starting_surface-1)+"i":
                    #print concerned_dimere
                    #print Cycling_letter_moving_A + str(int(elements_before[0][1:3])-Number_of_step_on_starting_surface-1)+"i"
                    n_parallel +=0
                else:
                    if int(concerned_dimere[1:3]) <= int(elements_before[4][1:3]):
                        n_parallel += 1
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                if concerned_dimere == "A21i":
                    print "Etot moving", E_tot
                return k0*np.exp( - E_tot * q / (kb * T) )     

        #######################################
        #    Cycling Up and Cycling Jump Up   #
        #######################################
        
        if is_in_bulk < 4 and (process_number % Nb_processes_per_type == 26 or process_number % Nb_processes_per_type == 28) :
            
             n_parallel = 0
             n_normal = 0
             
             Move_A = (dimere_type == 'A')
             Move_B = (dimere_type == 'B')
             #print "cycling up" 
             
             #no elements_before 1 because this process only happend if there is no upper atoms
             if Move_A:
                if int(concerned_dimere[1:3]) <= int(elements_before[2][1:3]):
                    n_parallel += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[3][1:3]):
                    n_parallel += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[4][1:3]):
                    n_normal += 1
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                if concerned_dimere == "A21i":
                    print "Etot cycling up", E_tot
                return k0*np.exp( - E_tot * q / (kb * T) )
             
             if Move_B:
                 if int(concerned_dimere[1:3]) <= int(elements_before[2][1:3]):
                     n_normal +=1
                 if int(concerned_dimere[1:3]) <= int(elements_before[3][1:3]):
                     n_normal +=1
                 if int(concerned_dimere[1:3]) <= int(elements_before[4][1:3]):
                     n_parallel += 1
                 E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                 if concerned_dimere == "A21i":
                     print "Etot cycling up", E_tot
                 return k0*np.exp( - E_tot * q / (kb * T) )
        
        if is_in_bulk >= 4 and (process_number % Nb_processes_per_type == 26 or process_number % Nb_processes_per_type == 28):
            return 0
        ###########################################
        #    Cycling Down and Cycling Jump Down   #
        ###########################################
        
        if is_in_bulk < 4 and (process_number % Nb_processes_per_type == 27 or process_number % Nb_processes_per_type == 29) : 
            
            n_parallel = 0
            n_normal = 0
            
            Move_A = (dimere_type == 'A')
            Move_B = (dimere_type == 'B')
            #print "cycling down"
            
            #no elements_before 4 because this process only happend if there is no lower atoms
            if Move_A:
                if int(concerned_dimere[1:3]) <= int(elements_before[1][1:3]):
                    n_normal += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[2][1:3]):
                    n_parallel += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[3][1:3]):
                    n_parallel += 1
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                if concerned_dimere == "A21i":
                    print "Etot cycling down", E_tot
                return k0*np.exp( - E_tot * q / (kb * T) )
                  
            if Move_B:
                if int(concerned_dimere[1:3]) <= int(elements_before[1][1:3]):
                    n_parallel += 1
                if int(concerned_dimere[1:3]) <= int(elements_before[2][1:3]):
                    n_normal +=1
                if int(concerned_dimere[1:3]) <= int(elements_before[3][1:3]):
                    n_normal +=1
                E_tot = E_substrate + n_normal * E_normal + n_parallel * E_parallel
                if concerned_dimere == "A21i":
                    print "Etot cycling down", E_tot
                return k0*np.exp( - E_tot * q / (kb * T) )
            
        if is_in_bulk >= 4 and (process_number % Nb_processes_per_type == 27 or process_number % Nb_processes_per_type == 29) :
            return 0
            
        
    def cutoff(self):
        """ Determines the cutoff for this custom model """
        return 1.0

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
number_of_steps1=1
control_parameters = KMCControlParameters(number_of_steps=number_of_steps1,
                                          dump_interval=1,
                                          seed=596312)
t1 = time.clock()
name = "Results_steps_%lg" %number_of_steps1 + "_Flux_%lg" %SendFlux + "_T°C_%lg" %T + "_En_%lg" %E_normal + "_Ep_%lg.py" %E_parallel
model.run(control_parameters, trajectory_filename=name)
t2 = time.clock()

print "simu time = "
print t2 - t1



