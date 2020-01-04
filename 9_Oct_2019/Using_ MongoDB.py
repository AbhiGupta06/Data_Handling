# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:48:06 2019

@author: BSDU ADMIN
"""
import pymongo

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
#mydb = client.forsk_db

#client = pymongo.MongoClient("mongodb://forsktech:Forsk%40123@cluster0-shard-00-00-tdcf5.mongodb.net:27017,cluster0-shard-00-01-tdcf5.mongodb.net:27017,cluster0-shard-00-02-tdcf5.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
#mydb = client.forsk_db

client = pymongo.MongoClient("mongodb://Abhigupta06:Abhi0006@cluster0-shard-00-00-ti73g.mongodb.net:27017,cluster0-shard-00-01-ti73g.mongodb.net:27017,cluster0-shard-00-02-ti73g.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client.Abhishek_Gupta



def add_employee(, first, last, pay):
    unique_employee = mydb.Demo_1.find_one({"Name":Name, "first":first, "last":last, "pay":pay})
    
    
    mydb.Demo_1.insert_one(
            {
    "id" : idd,
    "first" : first,
    "last" : last,
    "pay" : pay
    })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.Demo_1.find()
    for i in user:
        print (i)


#Drop a collection in Mongo
#mydb.Demo_1.drop()

add_employee(1,'Sylvester', 'Fernandes', 50000)
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)


fetch_all_employee()


