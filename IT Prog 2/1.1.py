# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:27:26 2018

@author: Romeo
"""

import random as rnd

randomintger = rnd.randint(10,20)

stack = ["========O" for x in range(randomintger)]


while True:
        #player or computer first
        wamount = 0
        playeramount = int(input("How much do you want to withdraw?: "))
        if playeramount <= 0:
            wamount = 1
            print("invalid amount enterd")
            pass
        elif playeramount == 1:
            stack = stack [:-1]
            print("Player has drawn ", playeramount , " of matches")
        elif playeramount == 2:
            stack = stack [:-2]
            print("Player has drawn ", playeramount , " of matches")            
        elif playeramount == 3:
            stack = stack [:-3]
            print("Player has drawn ", playeramount , " of matches")            
        else:
            wamount = 1
            print("invalid amount enterd")
            pass
        if len(stack) == 0:
            print("Player lost")
            break
        
        if wamount == 1:
            pass
        else:
            if len(stack) > 9:
                computeramount = rnd.randint(1,3)
            elif len(stack) == 9:
                computeramount = 2
            elif len(stack) == 8:
                computeramount = 3
            elif len(stack) == 7:
                computeramount = 3
            elif len(stack) == 6:
                computeramount = 1
            elif len(stack) == 5:
                computeramount = 1
            elif len(stack) == 4:
                computeramount = 3
            elif len(stack) == 3:
                computeramount = 2
            elif len(stack) == 2:
                computeramount = 1
            else:
                print("You got me")
                computeramount = 1
            
            if computeramount == 1:
                stack = stack [:-1]
            elif computeramount == 2:
                stack = stack [:-2]            
            elif computeramount == 3:
                stack = stack [:-3]
            if len(stack) == 0:
                print("Computer lost")
                break
            print("Coputer has drawn ", computeramount , " of matches")
            print(len(stack) , "remaining Matches")
            for i in stack:
                print (i)