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
material = np.float() #materialbudget
out = np.float() #output of machine
costma = np.float() #Cost manager
workhours = np.float() #workhours
mb = np.bool() 
laborbu = np.float()
#machine A
if machine is "A":
    costma = t*42*200
    material = 25000 + (335*47+1520*119)
    labor = budget - material - costma
    workhours = 20*8*t*150
    laborbu=labor+costma
    if costma < (laborbu*0.12) and costma > (laborbu*0.08) and material < (budget*0.25):
        print("Budget ohne Lohn kosten des Spezialisten",labor)
        print("Arbeitsstunden",labor/175)
        print("Manager cost",costma)
        print("material cost",material)
        print("Manager above ",costma < (laborbu*0.12),"Manager below",costma > (laborbu*0.08),"material ratio ",material < (budget*0.25))
        print ("Go ahead")
    else:
        print("Budget ohne Lohn kosten des Spezialisten",labor)
        print("Arbeitsstunden",labor/175)
        print("Manager cost",costma)
        print("material cost",material)
        print("Manager above ",costma < (laborbu*0.12),"Manager below",costma > (laborbu*0.08),"material ratio ",material < (budget*0.25))        
        print("NO")
    
#machine b    
else:
    costma = t*42*200
    material = 40000 + (865*159)
    labor = budget - material - costma
    workhours = 20*8*t*175
    laborbu=labor+costma
    if costma < (laborbu*0.12) and costma > (laborbu*0.08) and material < (budget*0.25):
        print("Budget ohne Lohn kosten des Spezialisten",labor)
        print("Arbeitsstunden",labor/175)
        print("Manager cost",costma)
        print("material cost",material)
        print("Manager above ",costma < (laborbu*0.12),"Manager below",costma > (laborbu*0.08),"material ratio ",material < (budget*0.25))
        print ("Go ahead")
    else:
        print("Budget ohne Lohn kosten des Spezialisten",labor)
        print("Arbeitsstunden",labor/175)
        print("Manager cost",costma)
        print("material cost",material)
        print("Manager above ",costma < (laborbu*0.12),"Manager below",costma > (laborbu*0.08),"material ratio ",material < (budget*0.25))
        print("NO")
    