# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:23:57 2019

@author: BSDU
"""


"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters
    (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}

"""


user = "www.google.com"

dict1 ={}

for i in user:
    if i not in dict1:
        dict1[i] = 1
    
    else:
        dict1[i]+=1
        
print (dict1)

    