# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:43:40 2017

@author: Romeo
"""

import numpy as np
arr=[]
i=np.int(input("How many people? "))
c=i
b=0
while i>0:
    a=np.int(input("Age: "))
    b+=a
    i-=1
    
print("The average of your groups is: ",float(b/c))