# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:39:14 2017

@author: Romeo
"""

inp=input('Number  (seperate with " "):')
inp=inp.split(" ")
table= [ [ 0 for i in range(20) ] for j in range(20) ]

i=0
for r in range(20):
    for c in range(20):
        table[r][c]=int(inp[i])
        i+=1
tmax=0
for r in range(20):
    for c in range(20):
        #calcmax
        try:
            mval1=table[r][c]*table[r-1][c+1]*table[r-2][c+2]*table[r-3][c+3]
        except IndexError:
            mval1 =0 
        try:
            mval2=table[r][c]*table[r+1][c]*table[r+2][c]*table[r+3][c]
        except IndexError:
            mval2 =0
        try:
            mval3=table[r][c]*table[r+1][c+1]*table[r+2][c+2]*table[r+3][c+3]
        except IndexError:
            mval3 =0
        try:
            mval4=table[r][c]*table[r][c+1]*table[r][c+2]*table[r][c+3]
        except IndexError:
            mval4 =0
        #save max
        maxarr=[mval1,mval2,mval3,mval4]
        if maxarr.index(max(maxarr)) ==0:
            posdat=((r,c),(r-1,c+1),(r-2,c+2),(r-3,c+3))
            lmax=mval1
        elif maxarr.index(max(maxarr)) ==1:
            posdat=((r,c),(r+1,c),(r+2,c),(r+3,c))
            lmax=mval2
        elif maxarr.index(max(maxarr)) ==2:
            posdat=((r,c),(r+1,c+1),(r+2,c+2),(r+3,c+3))  
            lmax=mval3
        else:
            posdat=((r,c),(r,c+1),(r,c+2),(r,c+3))
            lmax=mval4
    if lmax > tmax:
        tmax=lmax
        posmax=posdat
print("Maxmimum value in Table is: ",tmax," Position of values: ",posmax)