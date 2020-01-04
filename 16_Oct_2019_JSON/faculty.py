# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:06:15 2019

@author: BSDU ADMIN
"""

import json


json_string = """
{
	"Name": {
		"Firs_Name": "Ashish",
		"Last_Name": "Sharma"
	},
	"Age": 35,
	"Phone_Number": ["8619844650", "8690944650"],
	"Subject": "Web Development",
	"Smoking": false,
	"Gendar": "Male",
	"Address": {
		"TempAdress": "Bhankrota Jaipur"
	}

}
"""

print(json_string)

with open("data_file.json", "w") as write_file:
    json.dump(json_string, write_file)    
with open("data_file.json", "r") as read_file:
    jsondata=json.load(read_file)
    print(jsondata)
    
    

