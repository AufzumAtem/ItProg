# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:33:55 2017

@author: Romeo
"""

xy = 2
x10 = 10
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

print(root(xy),x10)