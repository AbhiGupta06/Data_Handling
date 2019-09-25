"""
Python Intermediate - enumerate,  Function, any, all, Collections
"""


# Enumerate 

"""
A lot of times when dealing with iterators, we also get a need to keep a count 
of iterations.
Python eases the programmers’ task by providing a built-in function enumerate()
for this task.

Enumerate() method adds a counter to an iterable and returns it in a form of 
enumerate object.
This enumerate object can then be used directly in for loops or 
be converted into a list of tuples using list() method.

Syntax:
enumerate(iterable, start=0)

"""


# Python program to illustrate 
# enumerate function 
l1 = ["eat","sleep","repeat"] 
s1 = "geek"

for item in l1:
    print (item)
 
for item in s1:
    print (item)

index = 0
for item in l1:
    print (index, item)
    index += 1
    
    
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  
print (type(obj1) )
print (list(enumerate(l1)) )
  

print (list(enumerate(s1)))


# changing start index to 2 from 0 
print (list(enumerate(s1,2)))


# Python program to illustrate # enumerate function in loops 
l1 = ["eat","sleep","repeat"]    

index = 0
for ele in l1 :
  print("{} {} ". format (index, ele ))
  index += 1
  
  
# printing the tuples in object directly 
for ele in enumerate(l1):      
    print (ele)  
    print (type(ele))

# changing index and printing separately 
for index,ele in enumerate(l1):     
    print (index,ele) 


for index,ele in enumerate(l1,100):     
    print (index,ele) 


# Using the concept of enumeration to iterate the tuple 
names_of_days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )


for index, item in enumerate(names_of_days):
  print("{} : {} ". format (index, item ))
 

for step in enumerate(names_of_days):
  print("{} : {} ". format (step[0], step[1] ))
 

for step in enumerate(names_of_days):
    print("{} : {} ". format (*step))
    
#single * denotes tuple and ** denotes dictionary 
 


# Hands On 1  
"""
lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"]      
Since you're super hungry and super excited about lunch,
enumerate over the array and append an "!" ("exclamation mark") 
to each menu item. 
"""
lunch_menu = ["pizza", "sandwich", "sushi", "soup", "salad"]  
print (type(lunch_menu) )
print (list(enumerate(lunch_menu)) )




# Hands On 2  
"""
nums = [1, 2, 3, 4]
Enumerate over the array and return a new array of the
squares of those numbers.
"""

nums = [1, 2, 3, 4]

for index,n in enumerate(nums,1):
    print(index," ",n**2 )
    
    
# Hands On 3  
"""
odds_and_evens = [1, 3, 2, 18, 5, 10, 24]
iterate over the array and return any even numbers. 
iterate over the array and return only the first array element that is odd

"""
odds_and_evens = [1, 3, 2, 18, 5, 10, 24]

for index,x in enumerate(odds_and_evens):
    if x%2==0:
        print(x , "Even")

for index,y in enumerate(odds_and_evens):
    if y%2!=0:
        print(y, "Odd" )
    
# Hands On 4  
"""
cats_and_dogs = ["cat", "cat", "dog", "cat", "dog", "dog"]
We all know that cats and dogs don't get along. 
Iterate over the array and delete the elements that represent dogs.
"""
cats_and_dogs = ["cat", "cat", "dog", "cat", "dog", "dog"]

while "dog" in (cats_and_dogs):
    cats_and_dogs.remove("dog")
print(cats_and_dogs)

# Hands On 5  
"""
famous_cats = ["Maru", "Lil Bub", "Grumpy Cat"]
check and see if the array includes the string "Maru"
"""
famous_cats = ["Maru", "Lil Bub", "Grumpy Cat"]

for i in famous_cats:
    if i=="Maru":
        print("True")

# Hands On 6
"""
quiet_and_loud = ["hi", "HI", "shhh", "WHAT?!"]
terate over the array to determine if any of the words contained there are loud (upcased).
"""
quiet_and_loud = ["hi", "HI", "shhh", "WHAT?!"]

for x in quiet_and_loud:
    if x == x.upper():
        print(x)
        
        
   
"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
  Hint:
      Try to use enumerate
"""

user = input("Enter the number")

while i in len(user):
    if i[1] == 13:
        
        
    
    



"""
Introduction to Function 


Functions are group of statements which perform specific tasks 
Functions reduce repetition of code 
Functions can be used to extend functionality in future 
Keep your code Dry ( Don’t Repeat Yourself ) 

"""


# Explain the calling of the function with the example of outsourcing your work to someone else ,
# Take Ashwani use case for taking attendance 

# Calling a global function
c = len("Test")
print(c)

print ( len ("Test") ) 


#Defining an empty function 
def hello_func():
  pass


#Calling the function 
hello_func()
 
# Printing the calling of the function will print None since our function is not returning anything 
print ( hello_func() ) 

# if we miss the () then it will not execute or 
# run the function but will print the address of the function 
hello_func

id(hello_func)



#Defining the function 
def hello_func():
  print ('Hello Forsk')


#Calling the function 
print ( hello_func() ) 



#Defining the function with return statements 
def hello_func():
  return 'Hello Forsk'


#Calling the function 
print ( hello_func() ) 



#Defining the function with argument 
def hello_func(greeting):
  return 'Welcome {}'.format ( greeting ) 


#Calling the function 
print ( hello_func("Sylvester") ) 


#Best Practice 
print ( hello_func(greeting = "Sylvester") ) 



#Defining the function with argument and default 
def hello_func(greeting, name ='You' ):
  return '{} {} Function'.format ( greeting, name ) 


#Calling the function 
print ( hello_func("Sylvester") ) 

print ( hello_func("Sylvester","Fernandes") ) 

print ( hello_func(greeting="Sylvester",name="Fernandes") ) 

print ( hello_func(name="Fernandes", greeting="Sylvester") ) 



#Introduce the concept of doc string for documentation of the function 
def hello_func(greeting, name ='You' ):
    """ My Greeting function """
    return '{} {} Function'.format ( greeting, name ) 


#Calling the function 
print ( hello_func("Sylvester") ) 

help(hello_func)
  
    

# Hands On 1  
# Make a function to find whether a year is a leap year or no, return True or False 

# Hands On 2
# Make a function days_in_month to return the number of days in a specific month of a year



"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""
user = input("Enter The Name")

def reverse(user):
    if len(user) == 0:
        return(user)
    else:
         return reverse(user[1:]) + user[0] 
     

print(user)
print(reverse(user))


"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse2.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a integer.
    Take input from User  
  Input: 
    -321
  Output:
    -123  
"""
user1 = input("Enter the number")

def reverse(user1):
    if len(user1)==0:
        return(user1)
        
    else:
        return reverse(user1[1:]) + user1[0]

print(user1)

print(reverse(user1))
"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""



"""
Any & All in Python

Any and All are two built-ins provided in python used for successive And/Or.

Any

Returns true if any of the items is True. 
It returns False if empty or all are false.
Any can be thought of as a sequence of OR operations on the provided iterables.
It short circuit the execution i.e. stop the execution as soon as the result is known.

"""


# Since all are false, false is returned 
print (any([False, False, False, False])) 
  
# Here the method will short-circuit at the 
# second item (True) and will return True. 
print (any([False, True, False, False])) 
  
# Here the method will short-circuit at the 
# first (True) and will return True. 
print (any([True, False, False, True])) 


"""

All

Returns true if all of the items are True (or if the iterable is empty). 
All can be thought of as a sequence of AND operations on the provided iterables. 
It also short circuit the execution i.e. stop the execution as soon as the result is known.

"""


# Here all the iterables are True so all 
# will return True and the same will be printed 
print (all([True, True, True, True])) 
  
# Here the method will short-circuit at the  
# first item (False) and will return False. 
print (all([False, True, True, False])) 
  
# This statement will return False, as no 
# True is found in the iterables 
print (all([False, False, False])) 



"""

Truth table

+-----------------------------------------+---------+---------+
|                                         |   any   |   all   |
+-----------------------------------------+---------+---------+
| All Truthy values                       |  True   |  True   |
+-----------------------------------------+---------+---------+
| All Falsy values                        |  False  |  False  |
+-----------------------------------------+---------+---------+
| One Truthy value (all others are Falsy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| One Falsy value (all others are Truthy) |  True   |  False  |
+-----------------------------------------+---------+---------+
| Empty Iterable                          |  False  |  True   |
+-----------------------------------------+---------+---------+



"""
"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""




# Advanced Collection ( Counter, OrderedDict, NamedTuple ) 

# check the frequency of the words

words = ["one", "two", "one", "two", "three", "four", "one"]

freq = dict()

for word in words:
    if word in freq:
        freq[word] += 1
    else: 
        freq[word] = 1
print(freq)


for key in freq.keys(): 
    print (key, ":", freq[key])
 
for key,value in freq.items():
    print (key, ":", value)



# Using default dict
from collections import defaultdict

words = ["one", "two", "one", "two", "three", "four", "one"]

freq = defaultdict(int)

# We have removed the logic to check whether key is present or not
for word in words:
    freq[word] += 1
     
print(freq)
    
for key in freq.keys(): 
    print (key, ":", freq[key])
 
for key,value in freq.items():
    print (key, ":", value)



# Alternate solution using Counter class 
    
from collections import Counter

words = ["one", "two", "one", "two", "three", "four", "one"]
frequency = Counter(words)
print (frequency)

for key,value in dict(frequency).items():
    print (key,value)

 

# namedtuple
# Writing clean python

"""
When to Use Namedtuples

Namedtuples can be an easy way to clean up your code and to make it more 
readable by enforcing a better structure for your data.

I find, for example, that going from ad-hoc data types like dictionaries 
with a fixed format to namedtuples helps me express my intentions more 
clearly. Often when I attempt this refactoring I magically come up with 
a better solution for the problem I’m facing.

"""
    
import collections
# regular tuple 
# 55 represents RED, 155 represents GREEN and 255 represents BLUE 
color = ( 55, 155, 255 ) 
print ( color[0] ) # This leads to non readable tuples 


#Solution is NAMEDTUPLE
Color = collections.namedtuple('myForsk', ['red','green','blue'])

print (type(Color))

color = Color ( blue=255, green=155, red = 55 )

print (type(color))

print ( color[0] ) 

print ( color.red )


# Returning Multiple Values From a Function
"""
Functions return one thing. 
When we return multiple values, we’re actually creating a tuple and 
returning it (again, one value).

As the number of values to return grows, the code becomes harder to read. 
In particular I have the rule of thumb, that for more than 3 arguments, 
namedtuples should always be used instead.

"""

def fetch_data():
     return 42, 'jsmith', 'John', 'Smith'

# Or
     
from collections import namedtuple

UserRecord = namedtuple("myRecord", ('user_id', 'username', 'first_name', 'last_name'))

def fetch_data2():
    return UserRecord(42, 'jsmith', 'John', 'Smith')
    
mydata = fetch_data2()

print (type(mydata))    
print (mydata.user_id)      # instead of mydata[0]
print (mydata.username)     # instead of mydata[1]
print (mydata.first_name)   # instead of mydata[2]
print (mydata.last_name)    # instead of mydata[3]


"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""

 