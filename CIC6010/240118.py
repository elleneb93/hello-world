# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:53:52 2018

@author: md1eeb
"""

import matplotlib.pyplot as plt

data = [0,1,2,2,2,3,4]

plt.hist(data)
plt.show


import matplotlib.pyplot as plt
import numpy as np

file = open("hist.txt","r")

data=[]
filtered = []

for line in file:
    line = line.rstrip('\n') #remove line break
    data.append(float(line))
file.close()

th = np.mean(data) +2*np.std(data)

for item in data:
    if item<th:
        filtered.append(item)

plt.hist(data,50,normed=1,facecolor='green')
plt.show() #important for terminals, not needed for spyder
print(np.mean(data),np.std(data))

plt.hist(filtered,50,normed=1)
plt.show()
print(np.mean(filtered),np.std(filtered))

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[0,2,1,3,4,3,4]

plt.plot(x,y)
plt.show

plt.scatter(x,y)
plt.show

z=np.polyfit(x,y,1) #z=np.polyfit(x,y,deg) where deg= 1 = fit linear regression line, deg = 2->parabolic
fit = np.poly1d(z)
plt.plot(x,y,'mo',x,fit(x),'c--') #yo=yellowdots, --k=black dash line, c cyan, m magenta'r--','bs','g^', * +, '-' '--' '-.' ':' 'steps' | ...]
plt.show