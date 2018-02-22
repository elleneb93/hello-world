# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:01:20 2018

@author: md1eeb
"""
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
