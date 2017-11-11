# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:43:40 2017

@author: Romeo
"""

import numpy as np
from random import randint
r=0
g=np.int(0)
for r in range(0,10000):
    r+=1
    x = randint(0,10)
    n=np.int(0)
    while n < 100:
        i=randint(0,10)
        n+=1
        if i == x:
            g+=n
            break
print ("it took an average of",g/10000," tries to find x")