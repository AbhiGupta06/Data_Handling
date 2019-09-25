# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:14:13 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Facorial
  Filename: 
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""
import math

####factorial of a number
user1 = int(input("Enter the factorial =: "))

user2 = math.factorial(user1)

print("The factorial of a number = {}". format(user2))