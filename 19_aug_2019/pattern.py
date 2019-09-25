# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:59:14 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
      
"""





for i in range (0,5):
   
       print(" * "*i)

for x in range(5,0,-1):
    print(" * "*x)