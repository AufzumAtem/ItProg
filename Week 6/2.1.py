# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:34:55 2017

@author: Romeo
"""

import os
#goto foler
os.chdir("../Week 6/music_extension_example")
x = os.listdir()
i=len(x)

#assign variable for array
n=0
while n < i:
    y = x[n]
    n+=1
    if y.find(".MP3") > 0:
        z=y[0:len(y)-y.find(".MP3")+1]
        os.rename(y,(z+".mp3"))
            