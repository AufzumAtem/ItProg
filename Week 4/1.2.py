# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:43:40 2017

@author: Romeo
"""

import numpy as np
from random import randint

x = randint(0,10)
n=np.int(0)
while n < 1000:
    i=np.int(input("Your guess :"))
    n+=1
    if i == x:
        print("Correct the Number was ",x,". It took you ",n," guesses to find the correct number", end = "")
        break
    elif x<i:
        print("The number is smaller", end = "")
    else:
        print("The number is higher", end = "")