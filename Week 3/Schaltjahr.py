# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 08:43:20 2017

@author: Romeo
"""
import numpy as np

year = np.int(input("Year: "))

if (year/400).is_integer():
    print("True")
elif (year/100).is_integer():
    print("False")
elif (year/4).is_integer():
    print("True")
else:
    print("False")