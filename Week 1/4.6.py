# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:46:48 2017

@author: Romeo
"""

import numpy as np
import pylab as pl
import math as mt

p = mt.pi
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Ysin = np.cos(2 * X)
Ycos = np.cos(3*p) 
#pl.axes([0.025, 0.025, 0.95, 0.95])
pl.plot(X, Ysin, color='blue', alpha=1.00)
pl.plot(X, Ycos, color='green', alpha=1.00)
pl.xlim([-np.pi, np.pi])
pl.ylim([-2.5, 2.5])
pl.show()