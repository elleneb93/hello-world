# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:36:44 2018

@author: md1eeb
"""

#this line is the first
print ('Hello World')
#really polite
print('How Are You?')
#not so much
print('Meh')
 
#plus
print(4 + 5)
print(5/4)
print((5-7)*3)
print((6/2)<12)

#my variables
counter = 100 #an integer assignment
pi = 3.14 #a floating point
name = 'John' # a string

#print them
print(counter)
print(pi)
print(name)

a = 12
b = 3
print(a +b)
print(a-b)
print(a*b)
print(a/b)

x= input ('kdsufegfxbcue')
print(x)

#integer to float
counter = 100
string = '53'

#conversion int to float
counter = float (counter)
number = int (string)

print (counter)
print (number)


a = input('82')
b = input('3')

a = float(a)
b = float(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)

if a>b:
    print('a is larger')
else:
    print('b is larger')
    if a>0:
        print ('a is pos.')
    else:
        print('a is neg.')

#define a number
a = input('input angle:')
b = input('input 2nd angle:')
c = input('input 3rd angle:')

a = float(a)
b = float(b)
c = float(c)

total = (a+b+c)

if a>0 and b>0 and c>0:
    print('All positive!')
    if total==180:
        print('Possible triangle')
    else:
        print('sum of angles is not equal to 180*. Difference:')
        print(180 - total)
else:
    print ('Negative number(s) present')
    
""" """
message = input('Whats the message?')
n = input ('how many times do you want the message displayed?')

n= int(n)

for i in range(n):
    print(message)

""" """
n = input ('how many numbers to average?')
min_ = input('pick the lowest number:')
max_ = input('pick the largest number:')


n=int(n)
min_ = int(min_)
max_ = int(max_)
interval = (max_-min_)/n
interval=int(interval)
no= range(min_,max_,interval)
total = sum(no)
ave = total / n
print('output:',ave)


""" """
sum = 0
n=input('How many numbers would you like to enter?')

n=int(n)

for i in range(n):
    number = input('Enter a number:')
    number = float(number)
    sum = sum + number
    
print('output:',sum/float(n))
