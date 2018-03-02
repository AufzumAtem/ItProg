# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:34:02 2018

@author: Romeo
"""

#Person

class Person:
    
    def __init__(self, first, last, dob, hair):
        self.first = first
        self.last = last
        self.dob = dob
        self.hair = hair
        self.email = first + '.' + last + '@students.zahw.ch'
       
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


per_1 = Person("Romeo", "Moritzi", 1992, "Brown")
per_2 = Person("Test", "Person", 1994, "Black")



print(Person.fullname(per_1))
print(per_1.email)
print(per_1.hair)


print(Person.fullname(per_2))
print(per_2.email)
print(per_2.hair)