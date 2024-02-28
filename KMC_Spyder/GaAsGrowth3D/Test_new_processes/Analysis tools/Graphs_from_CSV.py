# # -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import numpy as np

path = "C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Arrival_test/"
file_name = "CSV_test.csv"


def retrait_diese(string_chain):
    #on retourne la liste et on enlève les caractères ' #' en fin de chaine (.rstrip)
    flip_modified_string_chain = string_chain[::-1].rstrip(' #')
    
    #on re-retourne la chaine modifiée
    modified_string_chain = flip_modified_string_chain[::-1]
    
    return modified_string_chain

with open(path+file_name, 'r') as f:
    
    lines = f.readlines()
    names=[]
    data=[]
    
    for x in lines:
        x_split = x.split(',')
        
        #cas des noms de colonnes de données
        if str(x[0][0]) == '#':
            #le premier nom contient forcément un '# ' en premier
            name_1st = retrait_diese(x_split[0])
            names.append(name_1st)
            
            #on ajoute les autres noms
            for i in range(1, len(x_split)):
                names.append(x_split[i].rstrip("\n"))
        
            #on crée une liste de donnée de la taille appropriée
            for i in range(len(names)):
                data.append([])
            
        #cas des données
        else:
            for i in range(len(names)):
                data[i].append(float(x_split[i].rstrip("\n")))
    data = np.asarray(data)


plt.plot(data[0], data[1],label="A type")
plt.plot(data[0], data[2],label="B type")
plt.plot(data[0], data[1]+data[2])
plt.legend()