# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:14:11 2018

@author: md1eeb
"""

file = open("asteroid.txt","r")
#file_list=[]
x=[]
y=[]
for line in file:
    line = line.rstrip('\n')
    line = line.split(' ')    
    if len(line)==2:
    x.append(line[0])
    y.append(line[1])
file.close()

#print(x)
#print(y)
#print(file_list)
#len(file_list)
#for line in file:

a1_p_x = x[0] 
a1_v_x = x[1] 
a1_p_y = y[0] 
a1_v_y = y[1] 
a2_p_x = x[2] 
a2_v_x = x[3] 
a2_p_y = y[2] 
a2_v_y = y[3]
    
#from math import sqrt
import numpy as np
#CONSTANTS (start position and velocity)
#x1=150.4
#y1=200.5
#vx1=4.9
#vy1=7.1
#x2=122.6
#y2=64.0
#vx2=5.2
#vy2=2.95

#import texttable as tt
#tab = tt.Texttable()
#headings = ['Time','Asteroid 1 x','Asteroid 1 y','Asteroid 2 x','Asteroid 2 y','Distance']
#tab.header(headings)
#time = []
#ax1 = []
#ay1 = []
#ax2 = []
#ay2 = []
#distance=[]

#t=20
#for i in range(1, t)
while d>=0:
    #distance of each from origin (pythagoras)
    for i in range(1, t):
#    ax1=x1+(t*vx1)
 #   ay1=y1+(t*vy1)
  #  ax2=x2+(t*vx2)
   # ay2=y2+(t*vy2)
#print(bx1,by1)
#print(bx2,by2)
        ax1.append(x1+(t*vx1))
        ay1.append(y1+(t*vy1))
        ax2.append(x2+(t*vx2))
        ay2.append(y2+(t*vy2))

        h1=np.sqrt((x1**2)+(y1**2))#distance between each
        h2=np.sqrt((x2**2)+(y2**2))
        d=np.sqrt((h1**2)+(h2**2))
        distance.append(d)
        time.append(t)
    if d==0:
        print(t)
        break
    
for row in zip(time,ax1,ay1,ax2,ay2,distance):
    tab.add_row(row)

s = tab.draw()
print (s)

""""""
file = open("asteroid.txt","r") 

x=[] 
y=[] 
for line in file: 
    line = line.rstrip('\n') 
    line = line.split(' ') 
    if len(line) == 2: 
        x.append(line[0]) 
        y.append(line[1]) 
        file.close()
        
a1_p_x = x[0] 
a1_v_x = x[1] 
a1_p_y = y[0] 
a1_v_y = y[1] 
a2_p_x = x[2] 
a2_v_x = x[3] 
a2_p_y = y[2] 
a2_v_y = y[3]
import numpy as np 

def distance(a1x, a1y, a2x, a2y): 
    return np.sqrt((a1x - a2x) ** 2+ (a1y - a2y) ** 2) 

result = [] 

for i in range(50): 
    a1x = a1_p_x + a1_v_x * i 
    a1y = a1_p_y + a1_v_y * i 
    a2x = a2_p_x + a2_v_x * i 
    a2y = a2_p_y + a2_v_y * i 
    
    result.append(distance(a1x, a1y, a2x, a2y)) 
    
print(result)
    