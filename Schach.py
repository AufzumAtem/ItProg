# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:54:22 2017

@author: Romeo
"""

board = [[0 for c in range(8)] for r in range(8)]

#Spawn
w = [('T','W',0,0),('S','W',0,1),('L','W',0,2),('D','W',0,3),('K','W',0,4),('L','W',0,5),('S','W',0,6),('T','W',0,7),('B','W',1,0),('B','W',1,1),('B','W',1,2),('B','W',1,3),('B','W',1,4),('B','W',1,5),('B','W',1,6),('B','W',1,7)]
b = [('T','B',7,0),('S','B',7,1),('L','B',7,2),('D','B',7,3),('K','B',7,4),('L','B',7,5),('S','B',7,6),('T','B',7,7),('B','B',6,0),('B','B',6,1),('B','B',6,2),('B','B',6,3),('B','B',6,4),('B','B',6,5),('B','B',6,6),('B','B',6,7)]


for i in w:
    board[i[2]][i[3]] = (i[0],i[1])
for i in b:
    board[i[2]][i[3]] = (i[0],i[1])

checkmate = False

print('To input your turn please use Piece,x,y (K,2,2)')
#Moves
#while checkmate == False:    
    #Trun White
inpw = tuple(input('Turn White (use "," to separate): ').split(','))
    
    
    
    
    #Turn Black
inpb = tuple(input('Turn White (use "," to separate): ').split(','))
    
    
for j in board: 
        print(j)