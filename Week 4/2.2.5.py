# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 09:11:13 2017

@author: Romeo
"""
import collections as cl
import numpy as np
from random import randint
arr=[]
x = "x"
y = "."
rnd = int()
arr2=[]
i = np.int(input("How many times: "))
n=np.int(0)
#Rnd Generator
while len(arr)<15:
    rnd = randint(0,5)    
    if len(arr)==12 and y not in arr:
        for g in range(3):
            arr.append(y)
            g+=1
    elif y in arr:
        while len(arr)<15:
            arr.append(x)
    elif rnd == 1:
        for g in range(3):
            arr.append(y)
            g+=1
    else:
        arr.append(x)
#core function       
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