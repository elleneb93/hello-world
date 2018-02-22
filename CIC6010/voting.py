# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:32:11 2018

@author: md1eeb
"""

""" Voting"""

age= input('how old are you?')
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
        
