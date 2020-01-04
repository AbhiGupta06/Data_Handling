# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:14:45 2019

@author: BSDU ADMIN
"""


"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
"""

# Read the thanksgiving-2015-poll-data.csv file and 
#perform the following task :

import pandas as pd
import numpy as np

data = pd.read_csv("thanksgiving-2015-poll-data.csv")


#Convert the column name to single word names
clu = list(data.columns.values)
print(clu)

list1 = []
for i in range(0,65):
    list1.append('values'+ str(i))    
dict1 = {}
for i in range(0,len(list1)):
    dict1[clu[i]] = list1[i]

data.rename(columns = dict1, inplace=True)



###    Using the apply method to Gender column to convert Male & Female

data['values62'] = data['values62'].apply(lambda z : 1  if(z =='Male') else 0) 




## Using the apply method to clean up income
##(Range to a average number, X and up to X, Prefer not to answer to NaN)
import numpy as np
import math
def clean_income(value):
    if value == "$200,000 and up":
        return 200000
    
    elif value == "Prefer not to answer":
        return None
    elif isinstance(value, float):
        return None
    
    value = value.replace ('$',"")
    value = value.replace (",","")
    

    a,b = value.split(" to ")
    return (float(a) + float(b)) / 2

data["values63"] = data["values63"].apply(clean_income)
data["values63"].head()




"""compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?"""

demo1 =data[data["values8"] == "Homemade"]["values63"].mean()
demo2 =data[data["values8"] == "Canned"]["values63"].mean()

import pandas as pd
import matplotlib.pyplot as plt

list2 = data['values8'].value_counts()
lables = ['Homemade', 'Canned']

plt.pie([demo1,demo2], autopct ='%1.2f%%',labels=lables)

plt.show()


"""find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc)."""


import matplotlib.pyplot as plt


Home = data[data['values8'] == "Homemade"]['values63'].mean()
Cann = data[data['values8'] == "Canned"]['values63'].mean()
Non  = data[data['values8'] == "None"]['values63'].mean()
Other = data[data['values8'] == "Other (please specify)"]['values63'].mean()


list3 = data['values8'].value_counts()
lables = ['Homemade', 'Canned', 'None', 'Other' ]

plt.pie([Home,Cann,Non,Other], autopct ='%1.2f%%',labels=lables)

plt.show()


"""Do people in Suburban areas eat more Tofurkey than people in Rural areas?"""
import matplotlib.pyplot as plt

Subur = len(data[data['values60'] == 'Suburban']['values2'])
Rural = len(data[data['values60'] == 'Rural']['values2'])

plt.xticks([0,1],['Suburban','Rural'])
plt.bar([0,1],[Subur,Rural], color=["yellow","green"])

plt.show()


"""Where do people go to Black Friday sales most often?"""
    
friday_values = data[data['values57'] == "Yes"]['values64'].value_counts()
friday_name  = data[data['values57'] == "Yes"]["values64"].unique().tolist()

friday_name.pop()

# Pie Chart
plt.pie(friday_values, autopct ='%1.2f%%', labels = friday_name)
plt.show()


"""Is there a correlation between praying on Thanksgiving and income?"""

pyr   = data[data['values51'] == "Yes"]['values63'].mean()
Nopyr = data[data['values51'] == "No"]['values63'].mean()


plt.pie([pyr,Nopyr], autopct ='%1.2f%%',labels = ["Pyr", "Nopyr"])    
plt.show()


"""What income groups are most likely to have homemade cranberry sauce?"""  
        
Income = data[data['values8'] == "Homemade"]['values63'].value_counts().tolist()
val_incomes = list(data[data['values8'] == "Homemade"]["values63"].unique())

plt.pie([Income,val_incomes], autopct ='%1.2f%%',labels = ["Homemade", "Homemade"])    


    
"""  Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes"""

#  return all the values
data[data['values2']=='Turducken'][['values8','values63','values2']]

# homemade average income
one = data[(data['values2']=='Turducken') & \
           (data['values8'] == 'Homemade')
        ].mean()[-1]

# find all the values
data[data['values2']=='Roast beef'][['values63','values8','values2']]

# average income of Canned
two = data[(data['values8'] == 'Canned') & \
               (data['values63'] == data['values63'])
        ].mean()[-1]

# average income 
three = data[(data['values2'] =='Roast beef') & \
               (data['values8'] == 'Canned') & \
               (data['values63'] == data['values63'])
        ].mean()[-1]


verify_val = [one,two,three]

# plot 
plt.pie(verify_val,labels=['Homemade','Canned','Roast Beef'])


        
"""Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:"""