# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 07:52:08 2017
P02.1.1
@author: Romeo
"""
import numpy as np

n=np.int(5)    #range
r=np.int(0)     #fixed variable
arr=[]
arr2=[]
y="*"
# for loop n<=i print (x n time)
for r in range(n):
    if r< n/2:
        r +=1
        arr.extend(y)
        print(arr)
        
    else:
        r +=1
        arr2=arr[:-1]
        arr=arr2
        print(arr2)