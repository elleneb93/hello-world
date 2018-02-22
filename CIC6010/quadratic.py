# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:17:02 2018

@author: md1eeb
"""

def quad(a,b,c):
    
    x1=((-1*b) + ((b**2)-(4*a*c)**(1/2))/(2*a))
    x2=((-1*b) - ((b**2)-(4*a*c)**(1/2))/(2*a))
    
    return x1,x2
