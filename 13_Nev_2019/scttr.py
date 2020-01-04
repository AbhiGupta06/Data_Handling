# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:35:04 2019

@author: BSDU ADMIN
"""

import matplotlib.pyplot as plt

#Scatter

x = [1,2,3,4,5,6,7,8,9,10]

y = [1,2,3,4,5,6,7,8,9,10]


plt.title("A Scatter Graph")

plt.xlabel("X")
plt.ylabel("Y")

plt.grid()

plt.xlim(0,10)

plt.ylim(0,10)

plt.savefig("Scatter.jpg")

plt.plot(x,y , color = "green")

#plt.plot(x,y, linestyle = "dashed")

#plt.plot(x,y, '>' , color="red")

plt.scatter(x,y, marker='.', color='black', label="marker='{0}'".format('.'));
plt.legend(numponits=1)

plt.scatter(x,y)



plt.show()



