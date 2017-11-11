# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 07:52:08 2017
P02.1.1
@author: Romeo
"""
import numpy as np

i=np.int(3)
n=np.int(6)
r=np.int(0)
arr=["*"]
arr2=[]
y="*"
# for loop n<=i print (x n time)
for r in range(0, 5):
    if r< 3:
        r +=1
        print(arr)
        arr.extend(y)
    else:
        r +=1
        arr2=arr[:r-n]
        arr=arr2
        print(arr2)