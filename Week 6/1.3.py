# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 01:06:05 2017

@author: Romeo
"""
import random as rn
board= [[0 for c in range(10)] for r in range(15)]
ship=(rn.randint(0,14),rn.randint(0,9))
board[ship[0]][ship[1]]=1
outboard=[[0 for c in range(10)] for r in range(15)]
i=0
print(ship)
while i <10:
    i+=1
    guess=tuple(map(int,input('Insert guess use "," to separate: ').split(',')))
    try:
        board[guess[0]][guess[1]]
    except IndexError:
        print("Guess out of range")
        guess=tuple(map(int,input('Insert guess use "," to separate: ').split(',')))
    board[guess[0]][guess[1]]-=1
    if board[guess[0]][guess[1]]==0:
        print("Hit, you won")
        for c in range(10):
            for r in range(15):
                if board[r][c]==-1:
                    outboard[r][c]="X"
                
                else:
                    outboard[r][c]="0"
        outboard[guess[0]][guess[1]]="H"
        for j in outboard: 
            print(j)
        break
    else:
        print("Miss, try again")
        for c in range(10):
            for r in range(15):
                if board[r][c]==-1:
                    outboard[r][c]="X"
                
                else:
                    outboard[r][c]="0"
        for j in outboard: 
            print(j)
if i < 10:
    print("it took you ", i," tries to hit")
else:
    print("You lost, the ship was at: ", ship)