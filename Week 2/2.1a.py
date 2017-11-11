# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:13:14 2017

@author: Romeo
"""
import numpy as np
meA = np.float(900)
wpf = np.float(input("Weight of W Pilot/Passenger front:"))
wpr = np.float(input("Weight of Passenger rear:"))
wbc = np.float(input("Weight of baggage compartment:"))
wbt = np.float(input("Weight of Baggage tube:"))
wuf = np.float(input("Weight of Fuel:"))
mtow = np.float()

mtow = meA+wpf+wpr+wbc+wbt+wuf

if mtow > 1280:
    print("The plane is overweight, and not allowed to take off. Please remove ",mtow-1280,"kg of weight")
    
else:
    print("The plane is allowed to take off")