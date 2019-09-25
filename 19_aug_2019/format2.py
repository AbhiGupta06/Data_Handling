# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:38:45 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

#### input from the user 
user = "Welcome to Pink City Jaipur"

user1 = user.replace(" " , "*" )

print (user1)