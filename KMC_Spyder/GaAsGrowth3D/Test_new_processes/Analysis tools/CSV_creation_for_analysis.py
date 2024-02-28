# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import csv

path = "C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Arrival_test/"
file_name = "CSV_test.csv"

####################
#    Image size    #
####################

X = 40
Y = 120
Z = 100

####################

A_tot_list = []
B_tot_list = []

for i in range(len(types)):
    
	A_tot = 0
	B_tot = 0
    
	KMC_Result_current = types[i]
	for x in range(X):
		for y in range(Y):
			for z in range(Z):

				if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "A_GaAs":
					if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z + 1] == "V":
						A_tot += 1
                        
				if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "B_GaAs":
					if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z + 1] == "V":
						B_tot += 1
   
	A_tot_list.append(A_tot/(X*Y))
	B_tot_list.append(B_tot/(X*Y))


with open(path + file_name, 'w', newline='') as csvfile:
    fieldnames = ['#Times', 'A type coverage', 'B type coverage']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(times)):        
        writer.writerow({'Times': times[i], 'A type coverage': A_tot_list[i], 'B type coverage': B_tot_list[i]})
        