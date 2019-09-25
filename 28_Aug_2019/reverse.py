# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:36:46 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
user = input("Enter The Name --> ")

def reverse(user):
    if len(user) == 0:
        return(user)
    else:
         return reverse(user[1:]) + user[0] 
     

print(user)
print(reverse(user))
