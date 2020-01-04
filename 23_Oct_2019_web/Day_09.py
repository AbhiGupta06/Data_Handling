"""
Web Scrapping using BeautifulSoup and Selenium
"""

# Web Scraping with BeautifulSoup and Requests

# Parsing the content from the website and 
# pulling  the exact information you want
# Introduce to the page for Web Scrapping 

# pip install beautifulsoup4
# pip install lxml
# pip install html5lib

"""
Introduce the concept of basic HTML tags
HTML
  HEAD
    
  HEAD

  BODY
    
  BODY
HTML

"""

from bs4 import BeautifulSoup


# Create simple html files and 
# parse that using bs4 to make the students understand with title, div etc


html_file = open("simple.html")

soup = BeautifulSoup(html_file, "lxml")

print (soup)

print (soup.prettify())

print (soup.title)

print (soup.title.text)

print (soup.div)

print (soup.div.h1.text)

# Crome browser ( use the inspect tool to use the find function )
match = soup.find('div')
print (match)

match = soup.find("div", class_= "footer")
print (match)

print ( match.h2 )
print ( match.h2.text )

print ( match.p )
print ( match.p.text )

for article in soup.find_all("div") :
  headline = article.p.text
  print (headline)


# Give students a challenge to print some information from the HTML pages 




# Reading from the Internet
from bs4 import BeautifulSoup   
import requests

source = requests.get("http://httpbin.org/html").text
print(source)

soup = BeautifulSoup(source,"lxml")

print (soup)

print (soup.prettify())

print (soup.head)
print (soup.head.text)

print (soup.body)

print (soup.body.h1)
print (soup.body.h1.text)


print (soup.body.div)
print (soup.body.div.p)
print (soup.body.div.p.text)

"""
Web Scrapping using Selenium
"""

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")


all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='wikitable')

print (right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

my_table = right_table.findAll('tr')

print(my_table)

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())



from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")



"""
Real website data scrapping for Kerela Results
"""

#!pip install selenium

#Download 

#https://www.seleniumhq.org/download/
#installation for firefox
#https://github.com/mozilla/geckodriver/

#installation for chrome
#https://sites.google.com/a/chromium.org/chromedriver/



from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"


#For Windows System
browser = webdriver.Chrome("c:/chromedriver.exe")
#browser = webdriver.Firefox(executable_path="D:/geckodriver")

# For Mac System
#browser = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
#browser = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")


browser.get(url)

sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)


#get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result = browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/input[1]')

get_school_result.click()


sleep(10)
 
html_page = browser.page_source

soup = BS(html_page,"lxml")

# Now you can add your logic of reading from BeautifulSoup

sleep(10)


browser.quit()



"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
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






"""
THIS CODE IS NOT WORKING 


# Add Web Scrapping using Selenium
# pip install selenium


#Download 

#https://www.seleniumhq.org/download/
#installation for firefox
#https://github.com/mozilla/geckodriver/
#installation for chrome
#https://sites.google.com/a/chromium.org/chromedriver/




import pandas as pd
from selenium import webdriver

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"



#For Windows System
#driver = webdriver.Chrome("C:/Users/rohit/Downloads/chromedriver_win32/chromedriver.exe")
#driver = webdriver.Firefox(executable_path="D:/Forsk Technologies/geckodriver")

# For Mac System
#driver = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
driver = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")

# Opening the submission url
driver.get(wiki)



right_table=driver.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))

df = pd.DataFrame(col_data) 
df.to_csv("former.csv")



driver.quit()

"""

     
    
    
    


