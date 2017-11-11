# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 08:29:30 2017

@author: Romeo
"""

text =input("Input Text: ")
arr=[]
icount = 0
for a in text:
    arr.append(a)
    
for a in arr:
    b=1
    if a=="I" and arr[b-1]==" " and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="I" and arr[b-1]=="." and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="I" and arr[b-1]=="," and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="i" and arr[b-1]==" " and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="i" and arr[b-1]=="." and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="i" and arr[b-1]=="," and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="me" and arr[b-1]==" " and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="me" and arr[b-1]=="." and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="me" and arr[b-1]=="," and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="Me" and arr[b-1]==" " and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="Me" and arr[b-1]=="." and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="Me" and arr[b-1]=="," and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="my" and arr[b-1]==" " and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="my" and arr[b-1]=="." and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="my" and arr[b-1]=="," and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="My" and arr[b-1]==" " and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="My" and arr[b-1]=="." and arr[b+1]==" ":
        icount+=1
        b+=1
    elif a=="My" and arr[b-1]=="," and arr[b+1]==" ":
        icount+=1
        b+=1
    else:
        b+=1
    
print(icount)