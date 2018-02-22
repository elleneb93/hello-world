# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:06:06 2018

@author: UOS
"""

import matplotlib.pyplot as mpl
import random as r

def guess(y,minlim,maxlim):
    return r.randint(minlim,maxlim)
    #return int (((maxlim - minlim)/2) + minlim)

minlim = 0
maxlim=20
n=0#no attempts
y=[]#guess


while n < 11:
    print ('Think of a number between 0 and 20, I will guess!')
    y =(guess(y,minlim,maxlim))
    print y
    y.append(guess(y,minlim,maxlim))
    
    x=input ('Did I get it? (toohigh/ toolow/ correct):')

    if x == 'toohigh':
        maxlim==y
        n=n+1
        guess(y,minlim,maxlim)
        y.append(guess(y,minlim,maxlim))
        print('how about...', y)
    elif x == 'toolow':
        minlim==y
        guess(y,minlim,maxlim)
        n=n+1
        y.append(guess(y,minlim,maxlim))
        print('how about...', y)
    else:
        #ans == y
        print('great!, answer is:',y)
        mpl.plot(n,y,'ko')#n,ans,'co')#,x,fit(x),'c--') #yo=yellowdots, --k=black dash line, c cyan, m magenta'r--','bs','g^', * +, '-' '--' '-.' ':' 'steps' | ...]
        mpl.show()
        break

#if x == 'toohigh' :
 #   print('going lower')

#or x = 
 #           PCwon(x,y,n)    
 
# __author__ = 'Benoit'
#http://code.activestate.com/recipes/578963-guess-a-number-2-the-computer-attempts-to-guess-yo/
#Computer attempts to guess a number you choose between 1 and 100 in 10 tries
answer = 'yes'
print ("Please, think of a number between 1 and 100. I am about to try to guess it in 10 tries.")
while answer == "yes":
    NumOfTry = 10
    NumToGuess = 50
    LimitLow = 1
    LimitHigh = 20
    while NumOfTry != 0:
        try:
            print ("I try: ",NumToGuess)
            print ("Please type: 1 for my try is too high")
            print ("             2 for my try is too low")
            print ("             3 I guessed your number")
            HumanAnswer  = int (input("So did I guess right?"))
            if 1 < HumanAnswer > 3:
                print ("Please enter a valid answer. 1, 2 and 3 are the valid choice")
                NumOfTry = NumOfTry + 1
            if HumanAnswer == 1:
                LimitHigh = NumToGuess
                print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempts left")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 2:
                LimitLow = NumToGuess
                print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempts left")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 3:
                print ("Woo hoo! I won")
                NumOfTry = 0
        except:
            break
    else:
        answer = input ('Do you want to play again? (yes/no)')

else:
    print ("Thank you for playing. Goodbye")