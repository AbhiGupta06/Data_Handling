"""
Data wrangling using Pandas - Part 1
"""

'''Import Python Libraries'''
import pandas as pd


'''Create a Series from ndarray'''
import numpy as np
data = np.array(['a','b','c','d'])
print (type(data ))

s = pd.Series(data)
print (type(s))  
print (s)
# We did not pass any index, so by default, 
# it assigned the indexes ranging from 0 to len(data)-1, i.e., 0 to 3.


'''Customised Index value'''
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


'''Accessing Data from Series with Position'''
# Data in the series can be accessed similar to that in an ndarray.
# No doubt we have given indexes, but we are accessing using position 
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s)

#retrieve the first element
print (s[0])

#retrieve the first three element
print (s[:3])

#retrieve the last three element
print (s[-3:])


'''Accessing Data from Series with Index'''
# A Series is like a fixed-size dict in that you can 
# get and set values by index label.

# Retrieve Data Using Label (Index)
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s)

#retrieve a single element
print (s['a'])

#retrieve multiple elements
print (s[['a','c','d']])

#This will give KeyError
print (s['f'])



'''A Data frame is a two-dimensional data structure''' 
# data is aligned in a tabular fashion in rows and columns.
# You can think of it as an SQL table or a spreadsheet data representation


import pandas as pd


# Create a DataFrame from Lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df) 



# Create a DataFrame from List of Lists
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)


# Create a DataFrame from Dict of Lists
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)


data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)


print (df ['one'])
print (df ['one']['a'])

 

# Column Addition

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)


# Adding a new column to an existing DataFrame object with column label by passing new series
df['three']= pd.Series([10,20,30],index=['a','b','c'])
print (df)


#Adding a new column using the existing columns in DataFrame:
df['four']=df['one']+df['three']
print (df)


# Column Deletion
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print (df)


# using del function
del df['one']
print (df)


# using pop function
df.pop('two')
print (df)


# Drop rows with label 0
# df = df.drop(0)
# print (df)
# two rows were dropped because those two contain the same label 0.



# Row Selection by Label or index
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)

print (type(df.loc['b']))
print (df.loc['b'])
# The result is a series with labels as column names of the DataFrame.
# And, the Name of the series is the label with which it is retrieved.


# Selection by integer location or position
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)
print (type(df.iloc[1]))
print (df.iloc[1]) # position by default starts from 0 for the indexes 

 

import pandas as pd
#Read csv file
df = pd.read_csv("Salaries.csv")
#df = pd.read_csv("https://bitbucket.org/ntpl_sylvester/dataset/raw/467616310ddfaf8abbbbc13bdf1e32cdf0842cbd/Salaries.csv")


# Not a good technique to print the Data Frame
print (df)


df.info()


#number of dimensions
df.ndim   


#return a tuple representing the dimensionality
df.shape 


#number of elements
df.size 


#List first 5 records
df.head()


#Try to read the first 10, 20, 50 records;
#Can you guess how to view the last few records;


df.tail(5)


# Gives the row Indexes
df.index


#list the column names / column Indexes
df.columns 


#Check types for all the columns
df.dtypes


#list the row labels/index and column names
df.axes


#numpyrepresentation of the data
df.values 


# generate descriptive statistics (for numeric columns only)
# Standard Deviation is quite useful tool to figure out 
# how the data is spread above or below the mean.
# The higher the value, the less is reliable or vice versa. 
df.describe() # Numeric Columns
print(type(df.describe()))   
 

# This gives a missing values in salary and phd columns


# In order to see statistics on non-numerical features,
# include = all
df.describe(include=['object', 'bool','float64','int64'])
df.describe(include=['object', 'bool'])
df.describe(include=['float64','int64'])
df.describe(include=['object','float64','int64'])


#return max/min values for all columns
df.max() 
df.min()

#return max/min values for all numeric columns
df.mean()
df.median()
df.std()

#What are the mean values of the first 50 records in the dataset?
df.head(50).mean()

#returns a random sample of the data frame
df.sample(5) 




"""
Data Frames: method loc

If we need to select a range of rows, using their labels/index 
we can use method loc
"""

df.loc[:1]

df.loc[10:20,['rank','sex']]


"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""
df.iloc[:2]

df.iloc[ 10:21 , [0,4] ]


df.iloc[0] # First row of a data frame

df.iloc[1:5, :-1] # Leave last columns

df.iloc[:, 0] # First column

df.iloc[:, -1] # Last column

df.iloc[0:7] #First 7 rows

df.iloc[:, 0:2] #First 2 columns

df.iloc[1:3, 0:2] #Second through third rows and first 2 columns

df.iloc[[0,5], [1,3]] #1st and 6throws and 2nd and 4thcolumns


some_df = df.iloc[10:20,]
print(some_df)
some_df.head(10)

some_df.iloc[11:20,:]
some_df.iloc[0:10,:]

some_df.iloc[0]
some_df.loc[10]



# Position is starting from 0 onwards but the 
# index is same starting from 10 
some_df.loc[10:19,:]


"""
Selecting a column in a Data Frame with all rows
Method 1:
    Using iloc
    pd.iloc[:,2]

Method 2:
    Using loc
    pd.loc[:,"phd"]
    
Method 3: 
    Subset the data frame using column name like a dictionary:
    df['sex']

Method 4: 
    Use the column name as an attribute:
    df.sex

Note:there is an attribute rank for pandas data frames, 
"""

df.iloc[:,2]

df.loc[:,'phd']
 
# Read the data from a specific Series
df.phd
# Dont use this technique
df.rank

# This is the best practice 
df['phd']



#Select column rank and salary:
df[['rank','salary']]


# Find unique values in a Series / Column
df['rank'].unique()
df['discipline'].unique()
df['sex'].unique()
list1 = df['sex'].unique().tolist()


# intuition about a Rank Series
df['rank']
df['rank'].value_counts()

# to show in Percentage 
df['rank'].value_counts(normalize = True)


# To know the count of male and female candidates
df['sex'] 
df['sex'].value_counts()
df['sex'].value_counts(normalize = True)

# count missing values 
# ( It also counts the NaN Values in the Series/Column)
df['sex'].value_counts(dropna=False)

df['phd'].value_counts()
df['phd'].value_counts(dropna=False)

df['salary'].value_counts()
df['salary'].value_counts(dropna=False)


#calculate the basic statstics on the salary column
df['salary'].mean()
df['salary'].std()
df['salary'].describe()


#Find how many values in the salary column which are non NaN (use count method);
df['salary'].count()
df['phd'].count()

# Boolean Indexing
# Find those rows which has null values in salary/phd column
df['salary'].isnull()
df[df['salary'].isnull()]

df['phd'].isnull()
df[df['phd'].isnull()]
  

"""
Data Frames groupby method

Using "group by" method we can:
Split the data into groups based on some criteria
Calculate statistics (or apply a function) to each group
"""
#Group data using rank
df_rank= df.groupby(['rank'])

df_rank.size()
df_rank.count()
df_rank.groups
# Groups returns a dictionary object
df_rank.groups['AssocProf']
df_rank.groups['AssocProf'][0]

 
#group data using rank followed  by discipline and sex
df_rank=df.groupby(['rank', 'discipline','sex'])
df_rank.groups
df_rank.count()
 
#Calculate mean value for each numeric column per each group
df_rank.mean()


#Calculate mean salary for each type of professor rank:
df.groupby('rank')[['salary','phd']].min()
df.groupby('rank')[['salary','phd']].max()
df.groupby('rank')[['salary','phd']].mean()
        


"""
Data Frame: filtering

To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:

"""

# Boolean Indexing in Pandas
# select only those professors who has salary more than 120000
df['salary'] > 120000
df_sub= df[(df['salary'] > 120000) ]
df_sub

#or

df.loc[df['salary'] > 120000]


# to display only the selected series/column
df.loc[df['salary'] > 120000,'salary']



#filter using multiple columns

df_sub= df[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )
           ]
df_sub
# Or

df.loc[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )]



#Select only those rows that contain female professors:
df_sub = df[df['sex'] == 'Female' ][['salary','sex']]
df_sub

# Or

df.loc[df['sex'] == 'Female' ][['salary','sex']]



"""
DataFrame sorting
"""

# Create a new data frame from the original sorted by the column Salary
df_sorted= df.sort_values( by='service')
df_sorted.head()

# To find the lowest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [True])
df_sorted.head(1)


# To find the highest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [False])
df_sorted.head(1)


#We can sort the data using 2 or more columns:
df_sorted= df.sort_values( by=['service','salary'], ascending = [True,True])
df_sorted.head(10)

df_sorted= df.sort_values( by=['service','salary'], ascending = [True,False])
df_sorted.head(10)


"""
Missing Values

Missing values are marked as NaN
dropna(how='all') >> Drop observations where all cells is NaN
dropna(axis=1, how='all') >> Drop column if all the values are missing
dropna(thresh = 5) >> Drop rows that contain less than 5 non-missing values
fillna(0) >> Replace missing values with zeros
isnull() >> returns True if the value is missing
notnull() >> Returns True for non-missing values


Code to find missing values

total = df.isnull().sum(axis=1).sort_values(ascending=False)
percent = (df.isnull().sum(axis=1)/df.isnull().count(axis=1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total_missing_values_per_row', 'Percent'])
missing_data.head(20)

                                       

"""

df.info()

df[df['phd'].isnull()]

df[df['salary'].isnull()]



# mark zero values as missing or NaN
df['salary'] = df['salary'].replace(0, np.NaN)


#return a matrix by checking individual values
df.isnull()


#which column has null values in the Data Frame
df.isnull().any(axis=0)

#Check the rows that has atleast one NaN values
df.isnull().any(axis=1)

# Select the rows that have at least one missing value
df[df.isnull().any(axis=1)]

# Find those rows in which phd column has NaN
df[df['phd'].isnull()]

# Find those rows in which salary column has NaN
df[df['salary'].isnull()]

  

#There are a number of methods to deal with missing values in the data frame:
new_df = df.dropna()
new_df.count()

"""
Approach: Remove records (rows) that contain a missing value
df_copy = df.copy().dropna(how='any')
df_copy.shape


df_copy = df.copy().dropna(how='all')
df.shape"""


new_df2 = df.fillna(0)
new_df2.count()


# Fill All columns with missing values, with mean of that column
df = df.fillna(round(df.mean(),0))
df

# fill all the records with missing values, with mean of that column
df['phd'] = df['phd'].fillna(df['phd'].mean())

# fill all the records with missing values, with mean of that column
df['salary'] = df['salary'].fillna(df['salary'].median())



# How to drop columns
df.drop('discipline',axis=1, inplace=True)


# Remove the $ Sign from the Salary Column and then converted the string field into numeric
df['salary'] = df['salary'].str.replace('INR','').str.replace(',','')
df['salary'] = pd.to_numeric(df['salary'])


# Creating a new Column based on some other columns values 
# Male == 0 and Female == 1
df["bool_sex"] = df["sex"].map(lambda x: 0 if x == 'Male' else 1 )
df



#Value Conversion using apply function 
# Male == 0 and Female == 1

df = pd.read_csv("Salaries.csv")

def gender_code(gender_string):  
    if (gender_string == "Male") :
        return 0
    elif (gender_string == "Female") :
        return 1   
#    if isinstance(gender_string, float) and math.isnan(gender_string):

df["sex"].value_counts(dropna=False)

df["sex"] = df["sex"].apply(gender_code)

df["sex"].value_counts(dropna=False)


# Create a new column called df.Child where the value is yes
# if df.age is greater than 50 and no if not
df['child'] = np.where(df['age']<18, 'yes', 'no')


# Iterating over rows 
for i, row in df.iterrows():
    print("Index {}".format(i))
    print("Row \n{}".format(row))


