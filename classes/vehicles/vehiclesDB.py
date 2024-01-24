import sqlite3
from cars import Cars
from trucks import Trucks
from utilities import Utilities

# CRIAR VARIAS TABELAS PARA DIFERENTES VEICULOS
connection = sqlite3.connect("vehiclesDB.db")
cursor = connection.cursor()

def insertVehicles():

    global cursor

    selection = int(input())
    if selection == 1:
        id = int(input("car ID: "))
        licensePlate = input("License Plate: ")
        year = input("Year: ")
        weight = int(input("Weight: "))
        maintenance = input("Last maintenance date: ")
        mileage = int(input("Current Mileage: "))

        carObject = Cars(id=id, licensePlate=licensePlate, year=year, weight=weight, maintenance=maintenance, mileage=mileage)
        cursor.execute("""INSERT INTO cars VALUES 
        ('{}','{}','{}','{}','{}','{}')""".format(
            carObject.id, carObject.licensePlate, carObject.year, carObject.weight, carObject.maintenance, carObject.mileage))
        connection.commit()
        connection.close()

insertVehicles()