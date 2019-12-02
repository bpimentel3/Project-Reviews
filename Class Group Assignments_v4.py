# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:34:45 2019

@author: Brian Pimentel
"""

# Assign Students to Groups

import numpy as np
import pandas as pd
import random
import time
#import pandas as pd


t0 = time.time()

# number of students
groups = np.array([7,7,6,7,7,
                   7,6,7,7,6,
                   7,7,7,7,6,
                   7,7,7,7,7,
                   7,7,6,7,7,
                   7,7,7,7,5
                   ])

# Total number of students
n= groups.sum()

# Create data frame
students = pd.DataFrame(np.zeros((n,6)))
students.columns = ['Group', 'Assignment1','Assignment2','Assignment3',
                 'Assignment4','Assignment5']

# Distribute Group Numbers
a=0 # start index
b=0 # start index

for i, g_size in enumerate(groups):
    b += g_size
    students.iloc[a:b, 0] = i+1
    a = b

students.iloc[:,1:6] = np.resize(np.arange(1,31),
             students.iloc[:,1:6].transpose().shape).transpose()

# Create list of group assignments to be selected from
available = students.iloc[:,2].astype(int).tolist()
assignment=[]
size = len(available)

while size:
    index = random.randrange(size)      #Select random index
    elem = available[index]             #Get value of index

#Check it's not the same as own group number
    while elem == students.iloc[(len(students)-size),0]:    
            index = random.randrange(size)  #If same, reroll until not
            elem = available[index]
    available[index]= available[-1]         #Overwrite selected with last element
    del available[-1]                       #Delete last element
    size -=1                                #Reduce iterative variable
    assignment.append(elem)                 #Append selection to assignment list
        
students.iloc[:,1] = assignment


# Repeat selection, verify against duplicates

for turn in np.arange(2,6):
    available = students.iloc[:,turn].astype(int).tolist()
    assignment=[]
    size = len(available)
    
    while size:
        index = random.randrange(size)      #Select random index
        elem = available[index]             #Get value of index
#        count = 0
    #Check it's not the same as own group number
        while elem == students.iloc[(len(students)-size),0] or students.iloc[(len(students)-size),:turn].isin([elem]).any():    
                index = random.randrange(size)  #If same, reroll until not
                elem = available[index]
#                count +=1
#                if count >= 20:
#                    break
        available[index]= available[-1]         #Overwrite selected with last element
        del available[-1]                       #Delete last element
        size -=1                                #Reduce iterative variable
        assignment.append(elem)                 #Append selection to assignment list
    students.iloc[:,turn] = assignment


print(time.time()-t0)

    
    
    
    
    
    
    
    