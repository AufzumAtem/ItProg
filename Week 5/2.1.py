# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:43:57 2017

@author: Romeo
"""
x = input("Your input: ")
k = int(input("Key: "))
ed= int(input("1 for Encrypt, 2 for Decrypt: "))
text = []
out=[]

for a in x:
    text.append(a)
    
def encrypt(inp,i,k):
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",",]
    n=i
    res=[]
    g = inp[n]
    g = abc.index(g)
    f=int(g+k)
    z=int((f)/55)
    if z>=1:
        r=int(f-(z*55))
        res+=abc[r]
        return res;
    else:
        res+=abc[f]
        return res;

def decrypt(inp,i,k):
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",",]
    n=i
    res=[]
    g = inp[n]
    g = abc.index(g)
    f=int(g-k)
    z=int((f)/55)
    if z>=1:
        r=int(f-(z*55))
        res+=abc[r]
        return res;
    else:
        res+=abc[f]
        return res;
i=0
if ed == 2:
    for a in text:
        out+=decrypt(text, i,k)
        i+=1
    print(''.join(out))
elif ed ==1:
    for a in text:
        out+=encrypt(text, i,k)
        i+=1   
    print(''.join(out))
else:
    print("Encrypt Decrypt Value not recognised!")
