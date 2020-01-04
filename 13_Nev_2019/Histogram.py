# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:02:53 2019

@author: BSDU ADMIN
"""


import matplotlib.pyplot as plt


customerWaitTime = [43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,54.1,45.6,36.5,43.1]

customerWaitTime.sort()

print(customerWaitTime)

plt.hist(customerWaitTime, bins=[25,30,35,40,45,50,55], color="red")

plt.axis([25,60,0,6])

plt.xlabel("Seconds")
plt.ylabel("Customers")

plt.show()