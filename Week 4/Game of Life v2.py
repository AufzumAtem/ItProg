# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 22:53:39 2017

@author: Romeo
"""
from random import randint
n=int(input("how big is the matrix? "))
t=int(input("how many times? "))
xc, yc =[int(input("first adress: ")), int(input("second adress: "))]
t1=0
table= [ [ 0 for i in range(n) ] for j in range(n) ]
table2= [ [ 0 for i in range(n) ] for j in range(n) ]
table3= [ [ 0 for i in range(n) ] for j in range(n) ]
#seed
if xc<3 and yc<3:
    xc=3
    yc=3
elif xc<3:
    xc=3
elif yc<3:
    yc=3
elif xc+3>n:
    xc-=3
elif yc+3>n:
    yc-=3
    
table[xc][yc-3]=1
table[xc][yc+3]=1
table[xc+3][yc]=1
table[xc-3][yc]=1
table[xc-1][yc-2]=1
table[xc][yc-2]=1
table[xc+1][yc-2]=1
table[xc-2][yc-1]=1
table[xc-1][yc-1]=1
table[xc][yc-1]=1
table[xc+1][yc-1]=1
table[xc+2][yc-1]=1
table[xc-2][yc]=1
table[xc-1][yc]=1
table[xc][yc]=1
table[xc+1][yc]=1
table[xc+2][yc]=1
table[xc-2][yc+1]=1
table[xc-1][yc+1]=1
table[xc][yc+1]=1
table[xc+1][yc+1]=1
table[xc+2][yc+1]=1
table[xc-1][yc+2]=1
table[xc][yc+2]=1
table[xc+1][yc+2]=1
  
for j in table: 
    print(j)
print()
while t1 in range(t):
    t1+=1
    for r in range(n):
        for c in range(n):
            x=0
            if r == 0 and c == 0:
                x=table[r+1][c]+table[r][c+1]+table[r+1][c+1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            elif r==0 and c==n-1:
                x=table[r][c-1]+table[r+1][c-1]+table[r+1][c]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            elif c==0 and r==n-1:
                x=table[r-1][c]+table[r-1][c+1]+table[r][c+1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            elif r==n-1 and c==n-1:
                x=table[r-1][c]+table[r-1][c-1]+table[r][c-1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            elif c==n-1:
                x=table[r-1][c]+table[r-1][c-1]+table[r][c-1]+table[r+1][c]+table[r+1][c-1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            elif r==n-1:
                x=table[r-1][c]+table[r-1][c-1]+table[r][c-1]+table[r][c+1]+table[r-1][c+1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            elif r==0:
                x=table[r+1][c]+table[r][c+1]+table[r+1][c+1]+table[r][c-1]+table[r+1][c-1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            elif c==0:
                x=table[r-1][c]+table[r-1][c+1]+table[r+1][c]+table[r][c+1]+table[r+1][c+1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
            else: 
                x=table[r-1][c-1]+table[r][c-1]+table[r+1][c-1]+table[r-1][c]+table[r+1][c]+table[r+1][c+1]+table[r][c+1]+table[r-1][c+1]
                if x<2:
                    table2[r][c]=0
                elif x>3:
                    table2[r][c]=0
                elif x==3:
                    table2[r][c]=1
    for r in range(n):
        for c in range(n):
            if table2[r][c]==0:
                table3[r][c]=" "
            else:
                table3[r][c]="x"
   
    for r in range(n):    
        for c in range(n):
            if table2[r][c]==0:
                table[r][c]=0
            else:
                table[r][c]=1
    
    for j in table3: 
        print(j)
    
    print()