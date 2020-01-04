# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:23:09 2019

@author: BSDU ADMIN
"""

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0, 2.0, 0.01)
b = 1 + np.sin(2*np.pi*a)

plt.plot(a, b)



plt.xlabel('time (b)')
plt.ylabel('voltage (MV)')
plt.title('A Nice Sin Wave')
plt.grid()
plt.show()
