# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:06:46 2017

@author: Romeo
"""
import numpy as np
import math as mt

a = np.float(input("Calculate the square root of a="))
x1 = np.float(1)
n = np.int(10)

for n in range(0,n):
    x1 = x1 - (x1**2 - a) / (2*x1)

print ("square root is: ",x1)