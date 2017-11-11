# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:36:14 2017

@author: Romeo
"""

n = input("Input Credit Card number: ")
ccn=[]
c=[]
ccn2=[]
for a in n:
    ccn.append(a)
if ccn[4]==" " and ccn[9]==" " and ccn[4]==" " and len(ccn)==19:
    i=0
    ccn = [x for x in ccn if x != " "]
    ccn = [int(x) for x in ccn]
    if (sum(ccn)/10).is_integer():
        print("Credit Card is valid")
    else:
        print ("Credit Card numbers are not valid")


else:
    print("Credit Card format is not valid")

