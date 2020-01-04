
"""
JSON and Internet Libraries
"""
"""

JSON has become popular method for exchange of structured information over a 
network and sharing information across platforms.

It is basically text with some structure and saving it as .json

It stores data as key:value pairs.
Anything before : is called key and after : is called value.

This is very similar to Python dictionaries

You can see that the data are separated by , and that curly braces define objects.

Square brackets are used to define arrays in more complex JSON files

Other data types supported are string , number , boolean and null 

encoding is for writing data to disk ( serialisation )

decoding is for reading data into memory ( deserialisation ) 

The process of encoding JSON is usually called serialization.

Naturally, deserialization is the reciprocal process of decoding data that
 has been stored or delivered in the JSON standard.

Think of it like this: encoding is for writing data to disk, 
while decoding is for reading data into memory.

The following table is used to do a conversion from JSON Data types to Python Data Types

Python          JSON
dict            object  { }
list            array   [  ]
str             string  "  "
int             number  89, 98.67
True            true    true
False           false   false 
None            null    null


"""


# Loading raw json data into python specific data 
import json

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
print (type(json_string))

# Converts  JSON Data types to Python Data Types 
my_data = json.loads(json_string)

print (type(my_data) )  # its a python dictionary  , it uses the table to convert 
print (my_data) 
print (my_data['researcher'])

print (my_data['researcher']['relatives'])

print (my_data['researcher']['relatives'][0])

print (my_data['researcher']['relatives'][0]['name'])



# Converts Python Data types to JSON Data Types
new_json_string = json.dumps(my_data)

print (type(new_json_string) )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2 )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2, sort_keys=True)
print (new_json_string)



# Writing/Storing the JSON data in a File 

with open("data_file.json", "w") as write_file:
    json.dump(json_string, write_file)
    # json.dump(json_string, write_file, indent=2   )


# Reading from a JSON file

with open("data_file.json", "r") as read_file:
    jsondata=json.load(read_file)
    print(jsondata)
 
    # JSON in python data structure 
    my_data = json.loads(jsondata)
    print ( my_data)
    
    
"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""







# Get me the temperature of the city from the openweathermap.org

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

# Content in binary form
print (type(response.content))

print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))
print ("Data : " + response.text)

# Reading the Headers
for key, value in response.headers.items():
    print (key, ":" ,value , "\n")
   
print ("Content type: " + response.headers['content-type'])


print ("Content or Response Body : " + str(response.content))


# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
jsondata = response.json()
# response has the original JSON String
# jsondata has the convert string in the python data type dictionary

#print (str(type(jsondata)))
print (type(jsondata))


# Reading the JSON Data
print (jsondata)

print (jsondata.keys())

print (jsondata.values())

print (len(jsondata.items()))

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
   
jsondata["main"]["temp"]




# Sample code to POST data

import json
import requests

Host = "http://httpbin.org/post"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("http://httpbin.org/get?firstname=Dev&language=English")
    return response

print (get_method().text)



"""
How to use the urllib library
"""

    
import urllib
dir(urllib)  # contains (request, response,error,parse)

from urllib import request
dir(request)
 
   
resp = request.urlopen("https://www.wikipedia.org")
    
resp.code
    
resp.length  # in bytes
    
resp.peek() # its a byte object and not a string object
    
data = resp.read()   # reads entire response
    
type(data)
len(data)
    
html = data.decode('UTF-8')
    
type(html)
    
"""
# Introduce URL Encoding for Query String
qs = "key1=" + "value1" + "&" + "key2=" + "value2"
    
from urllib import parse
params = {"key1" :"value1", "key2" : "value2"} # create a dictionary
qs = parse.urlencode(params)
"""


"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""



"""
Code Challenge
  Name: 
    Next Bus
  Filename: 
    nextbus.py
  Problem Statement:
    Write a Python code to find when will the next bus come
    Try to make the program generalised so that is in not hard wired for bus route 22 and stop id 14787
    Also try if you can take the arguments from the command line
    Also try if you can run the program as a script from comand line
    
  Sample:
      Route 22 and Stop 14787
      Route 0 and Stop 5037
      
  Hint: 
    http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route=22&stop=14787 
"""

    