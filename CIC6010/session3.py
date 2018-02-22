# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:36:31 2018

@author: md1eeb
"""

def shutdown(s):
    if s == "yes" or s=="Yes"or s=="YES":
        return "shutting down"
    elif s == "no"or s=="No" or s=="NO":
        return "Shutdown aborted"
    else:
        return "Unknown parameter"
    
s = input ('Do you want to shut down?')
result = shutdown(s)
print (result)

def is_number(t):
    try:
        float(t)
        return True
    except ValueError:
        return False, "Input type error. Please input a number"

def distancefromzero(t):
    if type(t)==int or type(t)==float:
        return abs (t)
    else :
        return float(t)
        abs (t)
         #
t= input("type a number:")
check = is_number(t)
print(check)    

result = distancefromzero(t)
print (result)

#isinstance()