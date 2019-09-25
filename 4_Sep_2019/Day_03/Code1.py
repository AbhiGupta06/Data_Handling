# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:05:19 2019

@author: BSDU
"""

"""Find all of the numbers from 1-1000 that are divisible by 7"""

list_a = []

for i in range(1,1000):
   if i%7==0:
       list_a.append(i)  
print(list_a)


#why 2
list_b = [i for i in range(1,1000) if i%7==0]
print(list_b)


#why 3

list_c = filter(lambda i: i%7==0, range(1,1000))
print(list(list_c))


"""Find all of the numbers from 1-1000 that have a 3 in them"""

list_a = []
for i in range(1,1000):
    if str(3) in str(i):
        list_a.append(i)
print(list_a)


#why 2

list_b = [i for i in range(1,1000) if str(3) in str(i)]
print(list_b)

#why 3

#list_c = filter(lambda i: str(3) in str(i), range(1,1000))
#print(list_c)

"Count the number of spaces in a string"

user = (" Abhishek Gupta ")
count = 0 
for i in user:
    if i == ' ':
        count+=1
print(count)

#why 2

user = (" Abhishek Gupta ")
list_a =[i for i in user if (i.isspace)() == True]
print(len(list_a))





