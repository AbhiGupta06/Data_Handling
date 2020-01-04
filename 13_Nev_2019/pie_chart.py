# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:50:32 2019

@author: BSDU ADMIN
"""

import matplotlib.pyplot as plt

labels = "ML_AI", "IT", "ECE", "CSE"
sizes  = [14, 25, 20, 23]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = [0.1,0,0,0]



plt.pie(sizes, labels=labels,  colors=colors, explode=explode, autopct='%1.2f%%', shadow=True, startangle=90)

plt.axis("equal")

plt.savefig("pie_chart.jpg")
plt.show()