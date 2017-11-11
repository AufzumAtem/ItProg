# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:42:31 2017
2.1b
@author: Romeo
"""
import numpy as np
import math as mt

#input

machine = np.str(input("Machine A or B? "))
budget = np.float(input("Budget: "))
t = np.float(input("Duration: "))

#define values
labor = np.float() #laborbudget
materialt = np.float() #material total budget
material = np.float() #material budget
out = np.float() #output of machine
costma = np.float() #Cost manager
workhours = np.float() #workhours
share = np.int(0) #share of budget
pma = 42*200*t #Manager
#machine A

if machine is "A":
    for share in range(0,25):
        materialt = budget * share
        labor = budget - materialt
        if pma > (labor*.12) or pma < (labor*.08):
        share +=1
        else:
        workhours = labor / 150
        material = materialt - 25000
        material = 
                
    
    budget = workhours + manager + material + machine
    #Material
    
    print("Result A")
    
#machine b    
else:
    
    
    print("Result B")