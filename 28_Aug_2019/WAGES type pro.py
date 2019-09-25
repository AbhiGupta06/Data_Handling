# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:06:22 2019

@author: BSDU
"""

hours = float(input('enter hours worked:' ))
wage = float(input('enter dollars paid hour:'))
if hours <= 40:
   totalwage = wage*hours
else:
    overtime = hours - 40
    totalwages = wage*40 + wage*overtime
    
print('wage for hours are ' ,totalwages) 