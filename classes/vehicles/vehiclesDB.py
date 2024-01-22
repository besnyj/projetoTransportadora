import sqlite3

con = sqlite3.connect("vehicles.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE vehicles("
               "id INTEGER PRIMARY KEY, "
               "licensePlate TEXT, "
               "year TEXT, "
               "weight INTEGER,"
               "maintenaceHistory TEXT)")