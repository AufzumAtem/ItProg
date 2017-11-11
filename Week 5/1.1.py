# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:28:39 2017

@author: Romeo
"""
import math

def root(a):
    int(a)
    x1  = 1
    x2  = x1 - (x1**2 - a) / (2*x1)
    x3  = x2 - (x2**2 - a) / (2*x2)
    x4  = x3 - (x3**2 - a) / (2*x3)
    x5  = x4 - (x4**2 - a) / (2*x4)
    x6  = x5 - (x5**2 - a) / (2*x5)
    x7  = x6 - (x6**2 - a) / (2*x6)
    x8  = x7 - (x7**2 - a) / (2*x7)
    x9  = x8 - (x8**2 - a) / (2*x8)
    x10 = x9 - (x9**2 - a) / (2*x9)
    return x10;

x1 = int(input("x1:"))
y1 = int(input("y1:"))

x2 = int(input("x2:"))
y2 = int(input("y2:"))

d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
f=root(((x2-x1)**2)+((y2-y1)**2))   
print ("my function", f)

print ("correct result: ", d)