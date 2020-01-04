# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:56:54 2019

@author: BSDU ADMIN
"""

import requests


user = input("Enter The City Name ")

url = "http://api.openweathermap.org/data/2.5/weather?q="+user+"&appid=dc2f32efd25e5a68113cc63cc7cfb9b7"

#print(url)

response = requests.get(url)

response.content

jsondata = response.json()


temp = jsondata["main"]["temp"]
print(temp)


sys = jsondata["sys"]["sunset"]
print(sys)
 