# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:49:23 2017

@author: Romeo
"""

import os

os.chdir('C:\\Users\\Romeo\\Desktop\\ZHAW DOCS\\ItProg\\')

sitems = os.listdir()
flist = []
out = ["ItProg /"]
for l in sitems:
    os.chdir('C:\\Users\\Romeo\\Desktop\\ZHAW DOCS\\ItProg\\')
    if os.path.isdir(l) == True:
        flist.append(os.getcwd()+l)
        out.append(("|"+("- ")+ l + ("/")))
        os.chdir('C:\\Users\\Romeo\\Desktop\\ZHAW DOCS\\ItProg\\'+l)
        x=os.listdir()
        for s in x:
            out.append(("       |"+("--")+s))
    else:
        out.append(("|"+("- ")+l))        
for l in out:
    print(l)
'''
start = os.listdir()
adress = []
text = ["ItProg /"]

for l in start:
    adress.append(os.getcwd()+l)

for l in adress'''