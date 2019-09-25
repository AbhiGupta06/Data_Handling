# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:41:23 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

#########Assignment Max ############################
Assignment1 = float(input("Enter the 1 Assignment Max =: "))
Assignment2 = float(input("Enter the 2 Assignment Max =: "))
Assignment3 = float(input("Enter the 3 Assignment Max =: "))
E1 = float(input("Enter the 4 Assignment Max =: "))
E2 = float(input("Enter the 5 Assignment Max =: "))

########## Max Score ###################
weighted_score = ((( Assignment1 + Assignment2 + Assignment3 ) *0.1) + (E1 + E2 ) * 0.35)

print("Based on individual assignment scores = {}".format(weighted_score))
