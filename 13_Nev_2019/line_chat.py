# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:43:49 2019

@author: BSDU ADMIN
"""


""" Line Charts  """


import matplotlib.pyplot as plt

x = [10,20,30,40,50,60,70,80]

y = [10,20,30,40,50,60,70,80]


plt.title("A Line Chart")

plt.xlabel("X")
plt.ylabel("Y")

plt.grid()

plt.plot(x,y)

plt.show()