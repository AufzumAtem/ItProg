# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:13:29 2017

@author: Romeo
"""

start = eval(open('dictionary.txt').read())
remove = []

'''with open('dictionary.txt','r') as inf:
    dict_from_file = eval(inf.read())
    
list(start.keys())[0]'''
for n in start:
    print(n)
    inp = input("Please Translate the word above into German: ")
    if inp in start[n]:
        remove.append(n)
        print("Translation is correct, item removed")
    else:
        print("incorrect translation")
for n in remove:
    start.pop( n, None)
    
print("Remaining Dictionary: ", start)