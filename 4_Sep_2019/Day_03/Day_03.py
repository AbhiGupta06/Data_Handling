"""
Python Advanced - Deep Copy, Shallow Copy, List Comprehension, map, filter, reduce, lambda
"""

"""
When we use = operator user thinks that this creates a new object; well, it doesn’t. 
It only creates a new variable that shares the reference of the original object.

A shallow copy means constructing a new collection object and then populating 
it with references to the child objects found in the original. 
The copying process does not recurse and therefore won’t create copies of the child objects themselves


A deep copy makes the copying process recursive. It means first constructing a 
new collection object and then recursively populating it with copies of the 
child objects found in the original.
Copying an object this way walks the whole object tree to create a fully 
independent clone of the original object and all of its children.


Making a shallow copy of an object won’t clone child objects. 
Therefore, the copy is not fully independent of the original.

A deep copy of an object will recursively clone child objects. 
The clone is fully independent of the original, but creating a deep copy is slower.





"""

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

# So, if you want to modify any values in new_list or old_list, the change is visible in both.



# Shallow Copy 

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)


old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)



import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)



# Deep Copy

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)



import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)






"""
Four step process:
    Acquiring data from a source;
    Validating the data;
    Transforming the data; and
    Collecting the transformed data into a target container.

List comprehension (full immediate generation):
    [transform(datum) for datum in iterable if valid(datum)]

Set comprehension (full immediate generation):
    {transform(datum) for datum in iterable if valid(datum)}

Dict comprehension (full immediate generation):
    {keyFun(key): valFun(val) for key,val in iterable.items() if valid(key,val)}

Generator expression (generation on demand):
    (transform(datum) for datum in iterable if valid(datum))

"""


"""
List Comprehension 
"""

"""
List Comprehension is a handy and faster way to create lists in Python in just a single line of code. 
It helps us write easy to read for loops in a single line.

List comprehensions are used for creating new list from another iterables.
As list comprehension returns list, they consists of brackets containing 
the expression which needs to be executed for each element along with the 
for loop to iterate over each element.

for each_thing in a_group_of_things:
    do_something
    
Basic syntax:
new_list = [do_something for each_thing in a_group_of_things]

"""

# Find squares of a number using for loop.
squares = []

for n in range(1,5):
    squares.append(n**2)
print(squares)  


# Finding squares using list comprehensions
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)  



a = [1,2,3,4]
# [result_if_condition_met if condition else result_if_condition_not_met for element in group_of_elements]
[x for x in a if x % 2 == 1]

# Example for usage of if and else
# the syntax gets switched around once else is involved
[x+1 if x >= 5 else x+2 for x in a]


# Nested List Comprehension
a = [1,2,3,4]
print ([ x**2 for x in a ])
print ([ x + 1 for x in [x**2 for x in a ]])




# Skip this

# Find common numbers from two list using list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)


#List comprehensions can also be used to iterate over strings as shown below:
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [str.lower() for str in list_a]
print(small_list_a) # Output: ['hello', 'world', 'in', 'python']


# Just like tuples list comprehensions can be used to produce list of list as shown below.
list_a = [1, 2, 3]
square_cube_list = [ [a**2, a**3] for a in list_a]
print(square_cube_list) # Output: [[1, 1], [4, 8], [9, 27]]

# Skip uptill this


"""
Code Challenges

Find all of the numbers from 1-1000 that are divisible by 7

Find all of the numbers from 1-1000 that have a 3 in them

Count the number of spaces in a string

Remove all of the vowels in a string

Find all of the words in a string that are less than 4 letters

A list of all consonants in the sentence 'The quick brown fox jumped over the lazy dog'

A list of all the capital letters (and not white space) in 'The Quick Brown Fox Jumped Over The Lazy Dog'

A list of all square numbers formed by squaring the numbers from 1 to 1000.


"""


# Lambda

"""
Lambda is a way to create anonymous function i.e. functions without name 
Lambda function are mainly used with Filter, Map and Reduce 
Lambda operator or lambda function is used for creating small, 
one-time and anonymous function objects in Python.

Syntax:
lambda arguments: expression
This function can have any number of arguments but only one expression, 
which is evaluated and returned.

"""

 
# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y 

print(cube(5))


# Converting the function to lambda function  
g = lambda y: y*y*y 
print (type(g))
print(g(5))  


# Lambda with two arguments 
f  = lambda x,y : x + y
print(f(1,1))



# Add an exmaple to show the lambda with List Comprrehension



# Explain the concept of filter map reduce using the example of getting multiple  
# Temperature every sec using an IoT device


# Filter 
"""
The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence "sequence", 
for which the function returns True.
""" 

def f(x) :
    return x%3 ==0 or x%5 ==0 


my_list = list(range(2,25 ))
print(my_list)

my_filter_list = filter ( f, my_list)
print(list(my_filter_list))


# Filter with Lambda function 
my_filter_list = filter ( lambda x:x%3==0 or x%5==0, my_list)
print(list(my_filter_list))



# Map 

"""
map() function returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns :
Returns a list of the results after applying the given function to each item 
of a given iterable (list, tuple etc.) 
"""

# Return double of n 
def addition(n): 
  return n + n 

# We double all numbers using map() 
numbers = [1, 2, 3, 4] 
result = map(addition, numbers) 
print(list(result)) 


# Double all numbers using map and lambda 
numbers = [1, 2, 3, 4] 
result = map(lambda n: n + n, numbers) 
print(list(result)) 



# Skip this 

# Multiple iterables to the map function

# Add two lists using map and lambda 
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 


result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 


# List of strings 

l = ['sat', 'bat', 'cat', 'mat'] 
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 


# Skip uptill this 

# Need to get multiple integer inputs in the same line

#Way 1:
s = input()
print (s)
print(type(s))
s = s.split(',')
print(s)

s = [int(i) for i in s]
print(s)

#Way 2:
s = [int(i) for i in input().split(',')]
print(s)

#Way 3:
s = map(int, input().split(','))
print(list(s))


# How to use if within the map and lambda

list (map(lambda x: True if x % 2 == 0 else False, range(1, 11)))





# Reduce

"""
The reduce() function in Python takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the list. 
This is a part of functools module
"""


from functools import reduce

def add(x,y):
    return x+y

print (reduce ( add, [2,18,9,22,17,24,8,12,27]) )


# Reduce with Lambda function 
print (reduce (lambda x,y : x + y,[2,18,9,22,17,24,8,12,27]))


# zip

"""
In Python3, zip methods returns a zip object instead of a list. 
This zip object is an iterator. Iterators are lazily evaluated.
Lazy evaluation, or call-by-need is an evaluation strategy which 
delays the evaluation of an expression until its value is needed 
and which also avoids repeated evaluations
Iterators returns only element at a time. 
len function cannot be used with iterators. 
We can loop over the zip object or the iterator to get the actual list
"""


list_a = [1, 2, 3]
list_b = [4, 5, 6,7]

zipped = zip(list_a, list_b) # Output: Zip Object. <zip at 0x4c10a30>

len(zipped) # TypeError: object of type 'zip' has no len()

zipped[0] # TypeError: 'zip' object is not subscriptable

list_c = list(zipped) #Output: [(1, 4), (2, 5), (3, 6)]
print (list_c)

list_d = list(zipped) # Output []... Output is empty list becuase by the above statement zip got exhausted.
print (list_d)





"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
      import random

    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""




"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

      names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""



"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

      people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""






"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""


"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four fields from a table, containing:
          

          Rank,City,Population,State or union territory
          1,Mumbai,"124.42",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"124.42",Maharashtra
    9,Pune,"31.24",Maharashtra
    13,Nagpur,"24.05",Maharashtra
    6,Chennai,"46.46",Tamil Nadu
    59,Salem,"8.31",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":54.77}
    {"key":"India,Maharashtra","value":179.72}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra. 


    Refer to population.csv


"""





"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""


"""
Code Challenge

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

1 Get the corresponding `celsius` values in list

2 Create the `celsius` dictionary

3 convert a dictionary of Fahrenheit temperatures into celsius




Solution:
#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)


# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}
print(celsius_dict)


"""








# Create a new Code Challenge from this 
"""
stopchars = ['a', 'b', 'c', 'd']

def  normalize_word(word):
    word =  word.strip().lower()
    word = "".join([char for char in word if char not in stopchars])
    return word

stopchars = ['a', 'b', 'c', 'd']

def  normalize_word(word, stops=stopchars):
    word =  word.strip().lower()
    word = "".join([char for char in word if char not in stops])
    return word

"""