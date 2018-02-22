# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:58:55 2018

@author: md1eeb
"""

#import algebra

def largest(list1):
    return max(list1)

list1 = [4,6,2,4,8,12,7]

#print(algebra.largest(list1))

print('max:',max(list1), 'index:',list1.index(max(list1)))

#ImportError: cannot import name 'largest'

def my_max(numbers):  
    maximum = 0  
    maximum_index=0  
    for i in range(len(numbers)):    
        if maximum < numbers[i]:      
            maximum = numbers[i]      
            maximum_index = i  
        return maximum, maximum_index  
    
input_numbers = [4,6,2,4,8,12,7] 
print(my_max(input_numbers)) 


from algebra import sumofreciprocals
#def sumofreciprocals(N):
 #   sum = 0
  #  for i in range(1,N+1):
   #     if i>0:
    #        sum=sum+(1/i)
    #return sum

N=int(input('Type a positive number:'))
result=sumofreciprocals(N)
print(result)

#ImportError: cannot import name 'sumofreciprocals'

