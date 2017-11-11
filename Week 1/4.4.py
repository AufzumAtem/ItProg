# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:24:10 2017

@author: Romeo
"""
from math import sqrt

x1 = int(input("x1:"))
y1 = int(input("y1:"))

x2 = int(input("x2:"))
y2 = int(input("y2:"))

d=sqrt(((x2-x1)**2)+((y2-y1)**2))

print (d)