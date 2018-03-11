# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 13:51:37 2017

@author: Romeo
"""

a = ['a','b','c','d','a','c']

for i in a:
    if i == 'a':
        a.append('x')
    elif i == 'b':
        print("B")
    elif i == 'c':
        print("C")
    else:
        print("x")