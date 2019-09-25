# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:12:52 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
    
"""

x = input("Enter the input form User").split(",")

list1 =tuple(x)
print(x)
print(list1)

