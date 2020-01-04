# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:44:18 2019

@author: BSDU ADMIN
"""



"""
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like Student_Name, Student_Age, 
Student_Roll_no, Student_Branch.
"""






import sqlite3
from pandas import DataFrame


conn = sqlite3.connect ( 'university.db' )


c = conn.cursor()



c.execute("""CREATE TABLE university( 
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_Roll_No INTEGER,
          Student_Branch TEXT)""")

c.execute("DROP TABLE university")
conn.commit()

conn.commit()

c.execute("INSERT INTO university VALUES ('Abhishek', 18, 1806125001, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Anlit'   , 19, 1806125002, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Aswani'  , 19, 1806125003, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Chandu'  , 19, 1806125004, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Dk'      , 19, 1806125005, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Dinesh'  , 19, 1806125006, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Lakshey' , 18, 1806125007, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Lokesh'  , 18, 1806125008, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Nishu'   , 18, 1806125001, 'ML&AI' )")
c.execute("INSERT INTO university VALUES ('Riya'    , 18, 1806125001, 'ML&AI' )")


conn.commit()

c.execute("SELECT * FROM university")

print ( c.fetchone()) 

print ( c.fetchmany(2)) 
  
print ( c.fetchall() )


conn.close()
