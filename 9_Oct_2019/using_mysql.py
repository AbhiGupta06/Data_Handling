# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:37:14 2019

@author: BSDU ADMIN
"""


import mysql.connector




conn = mysql.connector.connect ( user='abhigupta', password='abhi0006', host='db4free.net', database = 'abhi_gupta')
c = conn.cursor()


#c.execute("DROP DATABASE IF EXISTS university;")
#conn.commit()

#c.execute("CREATE DATABASE university;")
#conn.commit()


#c.execute("USE university;")
#conn.commit()

c.execute("DROP Table university;")

c.execute("""CREATE TABLE university( 
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_Roll_No INTEGER,
          Student_Branch TEXT)""")

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

