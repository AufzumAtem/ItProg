# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:53:34 2017

@author: Romeo
"""
import re
start = open('settings.txt').read()
x = re.split("\n|=",start)
i = 0
d={}
while i < 5:
    d[format(x[i])]=int(x[i+1])
    i+=2

l=float(d['passengers_per_day ']/d['hours_per_day '])
u=float(d['average_service_rate_per_hour '])
#average number of customers in the system
ncs = l/(u-l)
#average number of customers in the queue
ncq = l**2/(u*(u-l))
#average waiting time in the system
wts = 1/(u-l)
#average waiting time in the queue
wtq = l/(u*(u-l))

f = open( 'results.txt', 'w' )
f.write( 'Customers in the system = ' + str(ncs) + '\n' )
f.write( 'avg number of customers = ' + str(ncq) + '\n' )
f.write( 'waiting time in the system = ' + str(wts) +'\n' )
f.write( 'avg waiting time = ' + str(wtq) + '\n' )
f.close()