# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:40:20 2019

@author: BSDU ADMIN
"""


"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""





from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

browser = webdriver.Chrome("c:/chromedriver.exe")

url = "https://bidplus.gem.gov.in/bidlists"

browser.get(url)

for i in range(1,11):
    bid_plus = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    A.append(bid_plus)
 
    items = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    B.append(items)
    
    Quantity_Required = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]').text
    C.append(Quantity_Required)
    
    D_and_A = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]').text
    D.append(D_and_A)
    
    Start_Date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text
    E.append(Start_Date)
    
    End_Date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    F.append(End_Date)
    
    
    
from collections import OrderedDict

col_name = ["BID NO"," items","Quantity Required","Department Name And Address","Start Date","End Date"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))    
    

import pandas as pd

df = pd.DataFrame(col_data)

df.to_csv("bid_plus.csv")
