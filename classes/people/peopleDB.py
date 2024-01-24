import sqlite3

con = sqlite3.connect("workers.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE workers ("
               "id INTEGER PRIMARY KEY ,"
               "name TEXT,"
               "age INTEGER,"
               "role TEXT,"
               "salary INTEGER,"
               "shift TEXT,"
               "department TEXT,"
               ""
               ")")