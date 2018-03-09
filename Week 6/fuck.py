# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:05:43 2017

@author: Romeo
"""
import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0, 5, 0.1);
amplitude = time%2
plot.plot(time, amplitude)