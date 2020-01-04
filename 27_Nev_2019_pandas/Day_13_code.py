"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""


"""1. Which Male and Female Professor has the highest and the lowest salaries"""

import pandas as pd

df = pd.read_csv("Salaries.csv")

print(df)

df.groupby('sex')[['salary']].min()

df.groupby('sex')[['salary']].max()


"""2. Which Professor takes the highest and lowest salaries."""

import pandas as pd

df = pd.read_csv("Salaries.csv")

print(df)

df.groupby['rank']

df[df['rank']=='Prof'][['salary']].min()
df[df['rank']=='Prof'][['salary']].max()

"""3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same"""
   
df[df['salary'].isnull()]

df['salary'][df['service']
x = df[df['service'] == 18]['salary'].mean() 

y = df[df['service'] == 2]['salary'].mean() 



"""5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage"""
   
import pandas as pd
import matplotlib.pyplot as plt

list1=df['sex'].value_counts()

lables=['female','male']

plt.pie(list1,autopct='%1.2f%%',labels=lables)

plt.show()


"""6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart"""

import pandas as pd
import matplotlib.pyplot as plt

list2 = df['rank'].value_counts()
lables = ['Prof', 'AsstProf', 'AssocProf']

plt.pie(list2, autopct ='%1.2f%%', labels=lables)

plt.show()


"""7. Who are the senior and junior most employees in the organization."""
import pandas as pd


"""
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K

"""

import pandas as pd
import matplotlib.pyplot as plt

list3 = df['salary'].dropna()

plt.hist(list3, bins=range(50000,200000,15000))


plt.show()