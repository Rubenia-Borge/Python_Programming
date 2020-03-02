#!/usr/bin/env python
# coding: utf-8

# In[6]:



# ----- Example Python program to create a database in PostgreSQL using Psycopg2 -----
# import the PostgreSQL client for Python

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# In[8]:


# Connect to PostgreSQL DBMS
con = psycopg2.connect("user=postgres password='sa'");
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);


# In[9]:


# Obtain a DB Cursor
cursor          = con.cursor();
name_Database   = "epidemiology";


# In[10]:


# Create table statement
sqlCreateDatabase = "create database "+name_Database+";"
# Create a table in PostgreSQL database
cursor.execute(sqlCreateDatabase);


# In[ ]:


# import the PostgreSQL adapter for Python
import psycopg2    

# Connect to the PostgreSQL database server
postgresConnection    = psycopg2.connect("dbname=test user=test password='test'") 

# Get cursor object from the database connection
cursor                = postgresConnection.cursor()
name_Table            = "news_stories" 

# Create table statement
sqlCreateTable = "create table "+name_Table+" (id bigint, title varchar(128), summary varchar(256), story text);" 

# Create a table in PostgreSQL database

cursor.execute(sqlCreateTable)
postgresConnection.commit()

# Get the updated list of tables
sqlGetTableList = "SELECT table_schema,table_name FROM information_schema.tables where table_schema='test' ORDER BY table_schema,table_name ;"

#sqlGetTableList = "\dt" 

# Retrieve all the rows from the cursor
cursor.execute(sqlGetTableList)
tables = cursor.fetchall()
# Print the names of the tables

for table in tables:
    print(table)

