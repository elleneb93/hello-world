# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:02:54 2018

@author: md1eeb
"""
import algebra as c

r=5

print(c.area(r))
print(c.circumference(r))


from algebra import area 
r=5 
print(area(r))


from algebra import quad as q

a=1
b=9
c=6

print(q(a,b,c))

from algebra import largest

list1 = [4,6,2,4,8,12,7]

print(largest(list1))

""""""

import numpy as np

print(np.roots([1,9,6]))

import numpy as np

a = [4,6,2,3,4,6,8,9,3,4,5,6,7]
print(np.mean(a))
print(np.var(a))
print(np.std(a))

""""""
file = open("test.txt","r")
file_list=[]

for line in file:
    file_list.append(line)
    
file.close()
print(file_list)

string = '1/n'
line = line.rstrip("\n")
print(line)

string = '1 3'
print(string)

split_string = string.split(' ')
print(split_string[0])
print(split_string[1])

file = open("wrong.txt","r")
result1=[]
result2=[]
for line in file:
    line = line.rstrip('\n')
    line = line.split(' ')
    result1.append(line[0])
    result2.append(line[1])
file.close()

print(result1)
print(result2)


