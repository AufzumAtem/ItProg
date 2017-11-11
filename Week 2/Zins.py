# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 09:27:49 2017

@author: Romeo
"""
import numpy as np
import math as mt

k = np.float(input("Kapital:")) #Kapital
z = np.float(input("Zinssatzt in %:")) #Zins
n = np.int(input("Number of Years:")) #Years

i = np.int(1)   #counter

z /=100
z +=1
for i in range (0,n):
    k *=z
    n +=1
    print("Kapital nach ",n," Jahren.")