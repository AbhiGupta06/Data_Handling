# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:20:45 2019

@author: BSDU ADMIN
"""

import pandas as pd

import numpy as np

data = np.array(['a','b','c','d'])
print(type(data))
print(data)

df = pd.Series(data)
print(type(df))
print(df)




#index

data = np.array(['a','b','c','d'])
demo1 = pd.Series(data, index =[101,102,103,104])
print(demo1)


demo1 = pd.Series(data, index= [101,102,103,104])

print(demo1)

print(demo1[0])

print(demo1[:1])

print(demo1[:3])


'''Accessing Data from Series with Index'''

demo1 = pd.Series([1,2,3,4,5,6], index = (['a','b','c','d','e','f']))

print(demo1)

print(demo1['a'])

print(demo1[['a', 'c', 'd']])

print(demo1['f'])




'''A Data frame is a two-dimensional data structure''' 


import pandas as pd

df = [1,2,3,4]
x = pd.DataFrame(df)
print(x)

data1 =[['Abhishek',19],['Ankit',20],['Aswani',21]]

x = pd.DataFrame(data,columns=['Name','Age'])

print(x)


# Create a DataFrame from Dict of Lists

data = {'Name':['Abhi','Jack', 'Steve', 'Ankit'], 'Age':[18,19,20,21]}
s  = pd.DataFrame(data)
print(s)


""" columns Addistion"""


s ={'one': pd.Series([1,2,3,], index =['a','b','c']),
        'two': pd.Series([1,2,3,4], index = ['a','b','c','d'])}

df = pd.DataFrame(s)
print(df)


df['three'] = pd.Series([10,20,30], index =['a','b','c'])
print(df)


df['four']=df['one']+df['three']
print(df)


import pandas as pd

data = pd.read_csv("Salaries.csv")

print(data)


data.info()