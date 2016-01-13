# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 18:25:55 2015

@author: nathy_000
"""
hours = -1
rate = -1
while (hours!=None and hours<0): 
    hours = raw_input("Enter Hours=")
    try:   
        hours = float(hours)
    except:
        hours = -1
    if (hours<0):
        print("Invalid hours input")

while (rate!=None and rate<0): 
    rate = raw_input("Enter Rate=")
    try:   
        rate = float(rate)
    except:
        rate = -1
    if (rate<0):
        print("Invalid rate input")

if (hours>40): 
    pay = (40 * rate) + ((hours-40)*(rate*1.5))
else:
    pay = hours * rate
    
print ("Pay= ") ,pay