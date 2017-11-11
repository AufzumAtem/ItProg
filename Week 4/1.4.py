# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:21:13 2017

@author: Romeo
"""

import math as mt
i=0
n=0
f=0
while n < 20:
    n+=1
    f+=(mt.factorial(4*i)/mt.factorial(i)**4)*((1103+26390*i)/396**(4*i))
    i+=1
       
c=((2*mt.sqrt(2))/9801)*f
c=1/c
print(c," ",mt.pi," ",c-mt.pi)