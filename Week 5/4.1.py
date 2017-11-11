# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 08:29:30 2017

@author: Romeo
"""

inp =input("Input Text: ")

def fpcount(text):
    text=text.split(" ")
    count=text.count("I")+text.count("i")+text.count("me")+text.count("Me")+text.count("My")+text.count("my")
    return count;

def wordcount(text):
    text=text.split(" ")
    return len(text);


def wordpsen(text):
    pos=([index for index, v in enumerate(text) if v == '.'])
    lenpos=len(pos)
    text=text.split(" ")
    avg=int(len(text)/lenpos)
    return avg;

#find the values
wc=wordcount(inp)
pc=fpcount(inp)
sc=wordpsen(inp)
if sc/(pc/wc)>300:
    print("The author of this text might be a woman based on the ratios. Wordcount: ",wc," Pronouns: ", pc," Words per sentence: ", sc," Pronoun ratio: ",pc/sc)
else:
    print("The author of this text might be a man based on the ratios. Wordcount: ",wc," Pronouns: ", pc," Words per sentence: ", sc," Pronoun ratio: ",pc/sc)
#Graveyard
    #inp=inp.split(" ")
    #pos=([index for index, v in enumerate(inp) if v == '.'])
    #lenpos=len(pos)
    #g=1
    #i=0
    #while g <= len(pos):
    #    n=pos[i]
    #    print(n)
    #    g+=1
    #    i+=1
    
    #while i >= len(inp):
    #    i=inp.index(".")
    #   len(inp[j:i])
    #   j=i
