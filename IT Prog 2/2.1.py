# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:22:43 2018

@author: Romeo
"""
import random as rn

class classroom:
    def __init__(self, documents):
        self.documents = documents
        self.blackboard = 0
        self.table = [0 for x in range(self.documents)]
    def handout(self):
        self.table = [1 for x in range(self.documents)]
        
#classroom.handout(20)