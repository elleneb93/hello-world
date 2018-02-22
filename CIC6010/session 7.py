# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:44:31 2018

@author: md1eeb
"""
import matplotlib.pyplot as plt
import random as r
import numpy as np

x=[]
y=[]

for i in range(100):
    x.append(i)
    y.append(i**2 + 20 + r.randint(0,1000))
   
plt.plot(x,y,'ko') 
plt.show()

z=np.polyfit(x,y,2) #z=np.polyfit(x,y,deg) where deg= 1 = fit linear regression line, deg = 2->parabolic
fit = np.poly1d(z)
plt.plot(x,y,'co',x,fit(x),'r--') #yo=yellowdots, --k=black dash line, c cyan, m magenta'r--','bs','g^', * +, '-' '--' '-.' ':' 'steps' | ...]
plt.show

""""""
file = open("SN_d_tot_V2.0.csv","r") 

x=[] 
y=[] 

for line in file: 
    line = line.rstrip('\n')
    line = line.split(';') 
    if float(line[3]) > 1987 and float(line[3]) < 2014: 
        if float(line[4]) != -1: #ignores lines with length =/=-1 
           x.append(float(line[3]))
           y.append(float(line[4]))
file.close()

plt.plot(x,y) 
plt.show()

z=np.polyfit(x,y,20) #z=np.polyfit(x,y,deg) where deg= 1 = fit linear regression line, deg = 2->parabolic
fit = np.poly1d(z)
plt.plot(x,y,'c',x,fit(x),'r--') #yo=yellowdots, --k=black dash line, c cyan, m magenta'r--','bs','g^', * +, '-' '--' '-.' ':' 'steps' | ...]
plt.xlabel('Date') 
plt.ylabel('SSN') 
plt.show()
