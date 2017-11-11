# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:42:31 2017
2.1b
@author: Romeo
"""
import numpy as np
import math as mt
t = np.int(input("Hours"))
e = ()

mata1 = np.int(input("Material A1:"))
mata2 = np.int(input("Material A2:"))
matb1 = np.int(input("Material B1:"))

#Labor
la=150*t
lb=175*t

ma = 25000
mb = 40000

machA=(mata1/47+mata2/119)/2
machB=(matb1/159)

mata1 =355*machA
mata2 =1529*machA
matb1 =865*machB


#Total cost
Print(ma+la+mata1+mata2+matb1+)