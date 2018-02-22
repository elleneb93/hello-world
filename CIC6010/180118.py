# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:56:25 2018

@author: md1eeb
"""

def circle_area (radius):
    Area = 3.14 *(radius **2)
    return Area

#call circle_area
result = circle_area(5)

print (result)



def is_positive(n): 
    if n >= 0:
        return True
    else:
        return False

n = input('Type a number:')
n=int(n)

result = is_positive(n)
print (result)

"""
def multiple (par):
    a= 3.14 * par
    b= 100 * par
    c= "Hi." *par
    return a,b,c

res1,res2,res3 = multiple(2)
"""

def arithmetic (n1,n2):
    add = n1 + n2
    subtract = n1 - n2
    multiply = n1 * n2
    divide = n1 / n2
    return add, subtract, multiply, divide

n1 = int(input('Type a number:'))
n2 = int(input ('Type another number:'))

add, subtract, multiply, divide = arithmetic(n1,n2)
print (n1, '+', n2, '=', add)
print (n1, '-', n2, '=', subtract)
print (n1, '*', n2, '=', multiply)
print (n1, '/', n2, '=', divide)

#2 methods to compare local vs global function "s"
def test_function():
    print(s)
    
s = "I hate spam" #defined in code

test_function()

def test_function():
    s = "I hate spam"
    return s #return variable if you need it later

result = test_function()
print (result)
    
""" """
list1 = ['physics', 'chemistry', 1997, 2000]
list2 =[1,2,3,4,5]
list3 = ["a", "b", "c", "d", "e"]

print (list1[0]) #0= 1st item in list
print(list2)
print(list3[3])
list1[2]=2001 #amend single item in list
print(list1)

list3.append(2005) #adds to end of the list
print(list3)

a = len([1,2,3]) #length
b = [1,2,3]+[4,5,6] #concatenation
c = ['Hi']*4 #repetition
print (a,b,c)

3 in [1,2,3] #membership

list = [1,2,3]
for element in list:
    print(element)
for iter in range(len(list)): #
    print(list[iter])
    
""" """
    
def average(_list):
    _ave =sum(_list)/(len(_list))
_list=[1,2,3,4,5,6,7,8,9]
print(_ave)

def listlength(listtocheck):
    if len(listtocheck)==0:
        return "is empty"
    else:
        return "is not empty"

test1=[1,2,3,4,5,6,7,8,9]
test2=[]

result1 = listlength(test1)
print ("test list 1",result1)

result2 = listlength(test2)
print ("test list 2", result2)
       
       
       




l=[]