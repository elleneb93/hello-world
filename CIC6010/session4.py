# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:56:11 2018

@author: md1eeb
"""
import random
def randomnum(a,b):
    if a==b:
        return "Good guess!"
    elif a>b:
        return "too low"
    else:
        return "too high"
        

a = random.randint(1, 9)
for i in range(3):   
    b = int(input ("select a number between 1 and 9:"))
    if a==b:
        break
ans = randomnum(a,b)
print (ans)

   
""" """
import random
n = int(input("how many chances?"))

def randomnum(a,b):
        if a==b:
            return "Good guess!"
        else:
            return "better luck next time"
        

for i in range(n):    
    a = random.randint(1, 9)
    b = int(input ("select a number between 1 and 9:"))
    ans = randomnum(a,b)
    print (ans, ", The number was:", a)
    if a==b:
        break
