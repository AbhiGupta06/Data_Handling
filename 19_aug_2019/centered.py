# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:36:01 2019

@author: BSDU
"""
"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
    
"""


x = input("Enter the input form User")

list1 = x.split(",")
list2 = []
for i in list1:
    num = int(i)
    list2.append(num)

list2.sort()
list2.pop()
list2.pop(0)

average = sum(list2)/len(list2)

print("Produce the final average = {}".format(average))


