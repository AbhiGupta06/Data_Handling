# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:32:32 2019

@author: BSDU ADMIN
"""

import json


json_string = """
{
	"Name": {
		"Firs_Name": "Abhishek",
		"Last_Name": "Gupta"
	},
	"Class": "ML&AI",
	"Age": 18,
	"Phone_Number": ["8619844650", "8690944650"],
	"DOB": "null",
	"Smoking": false,
	"Gendar": "Male",
	"Address": {
		"TempAdress": "Bhankrota Jaipur",
		"PermantAddress": "Bapu_Nagar_Ralia_Bhilwara"
	}

}

"""

print(json_string)

my_data = json.loads(json_string)

print(my_data["Name"])

print(my_data["Class"])

print(my_data["Address"]["TempAdress"])

print(my_data["Address"]["PermantAddress"])

print(my_data["Phone_Number"][0])