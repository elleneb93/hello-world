# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:22:33 2018

@author: md1eeb
"""

a = input('first:')
b = input('next:')

a = float(a)
b = float(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#integer no:
x= 435
y= 3 * x + 2
print(x)
print(y)
print (x,y)

x = '4'
y = 56
x = int(x) #now x is an integer
print (x)
x = float(x) #now x i s a float
print (x)

v1 = 3
v2 = 7
v3 = 32
v4 = 54
v5 = 12
v6 = 34

total = v1 + v2 + v3 + v4 + v5 + v6
ave = total / 6
print(ave)

st_1 = (v1 - ave)**2
st_2 = (v2 - ave)**2
st_3 = (v3 - ave)**2
st_4 = (v4 - ave)**2
st_5 = (v5 - ave)**2
st_6 = (v6 - ave)**2

std = st_1 +st_2+st_3+st_4+st_5+st_6
std = (std/6)**(1/2)
print(std)

""" """

x = 4**(1/2)
print(x)

string1 = 'Hello!'
string2 = "Python"
print(string1+string2)

miles = input('No. Miles:')
a = float(miles)
print(1.6*a)

km = input('No. Km:')
b= float(km)
print(b/1.6)