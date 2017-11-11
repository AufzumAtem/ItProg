# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 11:14:57 2017

@author: Romeo
"""
from random import randint

x= randint(1, 3)
y = input("Rock, Scissors or Paper? ")

a=x

if y == "Rock":
    b=1
elif y == "Scissors":
    b=2
else:
    b=3  

    
if x == 1:
   x = "Rock"
elif x == 2:
   x = "Scissors"
else:
   x = "Paper"

if a==b:
    z="It's a tie, play again!"
elif a == 1 and b == 2:
    z = "PC won!"
elif a == 2 and b == 3:
    z = "PC won!"    
elif a == 3 and b == 1:
    z = "PC won!"
else:f
    z = "You won!"   
    
print("You: ", y)
print("PC: ", x)
print("Result: ", z)
