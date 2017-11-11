# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 09:47:10 2017

@author: Romeo
"""
import math as mt
import scipy as sp
inp = [(1,1),(2,1),(2,2),(1,1)]

#calc 1
y = sp.spatial.distance.cdist(inp, inp, 'euclidean')

#sum matrix
n=len(inp)
out=0
i=0
while i < n-1:
    out += y[i][i+1]
    i+=1

#calc 2
a=len(inp)
l=0
d=0

while l < a-1:
    
    x1=inp[l][0]
    y1=inp[l][1]
    
    x2=inp[l+1][0]
    y2=inp[l+1][1]
    
    d+=mt.sqrt(((x2-x1)**2)+((y2-y1)**2))
    l+=1

print("With scipy: ",out)
print("With own formula :",d)