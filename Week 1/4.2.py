# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:09:24 2017

@author: Romeo
"""
v0 = float(input("speed :"))
mu = 0.3
g = 9.81
d = 0.5*(v0/3.6)**2/(mu*g)

print ("Dein bremsweg ist:",d)