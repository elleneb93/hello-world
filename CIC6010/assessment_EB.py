# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:06:45 2018
@author: UOS

Assessment info:
Write a program where the computer tries to guess the number you are thinking of,
instead of the other way around where you are guessing a computer's chosen number.
^ The computer has 10 attempts. 
^ Your number should be between 0 and 20.
^ You need to tell whether the guess is too high (th), too low (tl), or correct (c).
^ The output should be ‘the computer won’ or ‘you won’.
• The guess by the computer should not be based on random numbers! 
		NB. I've randomly generated the 1st guess too avoid a set pattern being generated but all later guesses are not. Can change if it's a problem.
^ Forming good coding habits (use functions, meaningful variable names, etc...).

Plot the guess vs attempt function!
^ Use matplotlib.
^ The function title is ‘the computer won’ or ‘you won’ depending on the situation.
^ Use black dots for visualisation. Do not forget to label the axes.
^ If the computer wins the last point on the graph will be the number you were thinking
of. This point must be displayed as being different from the others (i.e., different colour).
^ Save the figure (name: result.jpg).

"""

import matplotlib.pyplot as mpl
import numpy as np
import random as r
guess=[]

def computerwon(y,triesused):
    print("Great! I win.")
    print(y, "was your answer.")
    print("Got it in",triesused,"attempts.")
    print("Thanks for playing.")   
    
def computerfig(i,guess,y,triesused):
    fig, ax = mpl.subplots()
    ax.set_xlim([0.5,triesused+0.5])
    mpl.xlabel('No. of Guesses')
    mpl.ylabel('Value of Guess')
    mpl.xticks(i)    
    ax.set_ylim([0,21])
    ax.scatter(i,guess,c='0')
    ax.scatter(triesused,y,c='r')
    ax.axhline(y, xmin=0, xmax=1, ls='--', c='r')
    mpl.savefig('result.jpg',bbox_inches='tight')
    return mpl.show()    

def userwon(triesused):
    print("Look you win!")
    print("I used all",triesused, "attempts")
    print("I'll get you next time!")    

def userfig(triesused,i,minlim,maxlim):
    fig, ax = mpl.subplots()
    ax.set_xlim([0.5,triesused+0.5])
    mpl.xlabel('No. of Guesses')
    mpl.ylabel('Value of Guess')
    mpl.xticks(i)
    ax.set_ylim([0,21])
    ax.scatter(i,guess,c='0')
    ax.axhline(minlim, xmin=0, xmax=1, ls='--', c='r')
    ax.axhline(maxlim, xmin=0, xmax=1, ls='--', c='r')
    mpl.savefig('result.jpg',bbox_inches='tight')
    return mpl.show()    

print ("Please, think of a number between 1 and 20 and I'll guess it in 10 tries.")
n = 10 #no of tries
minlim = 1 #min number
maxlim = 20 #max number
y=r.randint(minlim, maxlim) #only random first guess
guess.append(y) #list of guesses
    
while n != 0:
        print("my guess is:",y)            
        x=input ('Did I get it? (toohigh/ toolow/ correct):')
        #if x not in {'toohigh', 'toolow' ,'correct'}:               
        #print ("Please enter a valid answer (toohigh/ toolow/ correct)")
        if x == 'toohigh':
            maxlim = y
            n=n-1
            print("so your number is between",minlim, " and ", maxlim)
            print(n, "attempts left")
            y=int(((maxlim - minlim)/2) + minlim) #guess
            guess.append(y) #list of guesses
        elif x == 'toolow':
            minlim=y
            n=n-1
            print("so your number is between",minlim, " and ", maxlim)
            print(n, "attempts left")
            y=int(((maxlim - minlim)/2) + minlim) #guess
            guess.append(y) #list of guesses
        elif x == 'correct':
            n=n-1
            triesused = 10-n
            i=list(np.arange(1,triesused+1))
            computerwon(y,triesused)
            computerfig(i,guess,y,triesused)
            break
else:
    triesused = 10-n
    guess = guess[:-1]
    i=list(np.arange(1,triesused+1))
    userwon(triesused)
    userfig(triesused,i,minlim,maxlim)    