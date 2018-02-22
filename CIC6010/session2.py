# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:32:11 2018

@author: md1eeb
"""

""" Voting"""

age = input('how old are you?')
age = float(age)

wtime = 18-age
rtime = 65-age

if age>18:
    print('You can vote!')
    if age<65:
        print('only this many years til retirement:')
        print(rtime,'yrs')
    else:
        print('Enjoy your retirement')
else:
        print('Sorry a few years to wait:')
        print(wtime, 'yrs')
        """ Voting"""

        
        
""" lamp"""

q1=input('Is the lamp plugged in? Y/N')
if q1 == 'N':
    print('Plug in the lamp')
    q2 = input('Is the lamp now working?')
    if q2 =='N':
        q3 = input('Is the bulb burned out?')
        if q3 == 'N':
            print('repair the lamp?')
        else: print('replace bulb.')
        q4 = input('Is the lamp now working?')
        if q4 == 'N':
            print('repair the lamp?')
        else: print ('good joba!')
    else: print('good job!b')
else: q2 = input('Is the lamp now working?')
if q2 =='N':
    q3 = input('Is the bulb burned out?')
    if q3 == 'N':
        print('repair the lamp?')
    else: print('replace bulb.')
    q4 = input('Is the lamp now working?')
    if q4 == 'N':
        print('repair the lamp?')
    else: print ('good jobc!')
else: print('good job!d')
