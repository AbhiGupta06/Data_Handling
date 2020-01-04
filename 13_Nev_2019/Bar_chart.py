# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:24:34 2019

@author: BSDU ADMIN
"""
import matplotlib.pyplot as plt

'''
obj = ("Python", "C++", "Java", "PHP", "Peral", "Scala")

Performance = [10,8,6,4,2,1]

plt.bar([0,1,2,3,4,5], Performance, align ="center", alpha = 1.0)

plt.yticks([0,1,2,3,4,5], obj)

plt.xlabel("Usage")

plt.title("Programing Language Usage")

plt.show()

'''


############################################

label = ['Adventure', 'Action', 'Drama', 'Comedy', \
         'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical', \
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', \
         'Multiple Genres', 'Reality']
 
no_movies = [941,854,4000,2125,942,509,548,149,1952,161,64,61,35,5]

index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

plt.bar(index,no_movies)
plt.xlabel('Grnre', fontsize=20)
plt.ylabel('No Of Movies', fontsize=15)
plt.xticks(index, label, fontsize=10, rotation=90)
plt.title("Market Share for Each Genre 1995-2017")

plt.show()