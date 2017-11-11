# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 09:11:13 2017

@author: Romeo
"""
import collections as cl
import numpy as np
arr=[".",".","x","x","x","x","x","x","x","x","x","x","x","x","x"]
arr2=[]
i = np.int(input("How many times: "))
n=np.int(0)
x = "x"
y = "."
while n < i:
    n+=1  
    counter =cl.Counter(arr)
    counter = counter.values()
    counter = list(counter)
    if arr[14]==y:
        arr.insert(0,y)
        arr2=arr[:-1]
        arr=arr2
        print(arr)
    elif counter[0]==3:
        arr.insert(0,x)
        arr2=arr[:-1]
        arr=arr2
        print(arr)
    elif counter[0]<3:
        arr.insert(0,y)
        arr2=arr[:-1]
        arr=arr2
        print(arr)
    elif arr[0]==x:
        arr.insert(0,x)
        arr2=arr[:-1]
        arr=arr2
        print(arr)