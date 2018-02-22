# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:04:08 2018

@author: md1eeb
"""

def largest(list1):
    return max(list1)
#use for loop to create and compare each index of list individually vs the existing max. first needs max=0 

def area(r):
    return 3.14*(r**2)

def circumference(r):
    return 2*3.14*r

def quad(a,b,c):
    
    x1=((-1*b) + ((b**2)-(4*a*c)**(1/2))/(2*a))
    x2=((-1*b) - ((b**2)-(4*a*c)**(1/2))/(2*a))
    
    return x1,x2

def sumofreciprocals(N):
    sumofvalues = 0
    for i in range(1,N+1):
        if i>0:
            sumofvalues=sumofvalues+(1/i)
    return sumofvalues