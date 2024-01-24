import sqlite3
from cars import Cars
from trucks import Trucks
from utilities import Utilities

# CRIAR VARIAS TABELAS PARA DIFERENTES VEICULOS
connection = sqlite3.connect("vehiclesDB.db")
cursor = connection.cursor()


def insertVehicles():

    print("Add new vehicle: \n1. Car \n2. Trucks \n3. Utility")

    global cursor

    selection = int(input())
    # car
    if selection == 1:
        id = int(input("Car ID: "))
        licensePlate = input("License Plate: ")
        year = input("Year: ")
        weight = int(input("Weight: "))
        maintenance = input("Last maintenance date: ")
        mileage = int(input("Current Mileage: "))

        carObject = Cars(id=id, licensePlate=licensePlate, year=year, weight=weight,
                         maintenance=maintenance, mileage=mileage)
        cursor.execute("""INSERT INTO cars VALUES 
        ('{}','{}','{}','{}','{}','{}')""".format(
            carObject.id, carObject.licensePlate, carObject.year,
            carObject.weight, carObject.maintenance, carObject.mileage))
        connection.commit()
    # truck
    if selection == 2:
        id = int(input("Truck ID: "))
        licensePlate = input("License Plate: ")
        year = input("Year: ")
        weight = int(input("Weight: "))
        maintenance = input("Last maintenance date: ")
        tripHistory = input("Date of last trip: ")
        truckObject = Trucks(id=id, licensePlate=licensePlate, year=year,
                             weight=weight, maintenance=maintenance, tripHistory=tripHistory)
        cursor.execute("""INSERT INTO trucks VALUES ('{}','{}','{}','{}','{}','{}')""".format(
            truckObject.id, truckObject.licensePlate, truckObject.year, truckObject.weight,
            truckObject.maintenance, truckObject.tripHistory
        ))
        connection.commit()
    # utilities
    if selection == 3:
        id = int(input("Vehicle ID: "))
        licensePlate = input("License Plate: ")
        year = input("Year: ")
        weight = int(input("Weight: "))
        maintenance = input("Last maintenance date: ")
        type = input("Type of utility car: ")
        utObject = Utilities(id=id, licensePlate=licensePlate, year=year,
                             weight=weight, maintenance=maintenance, type=type)
        cursor.execute("""INSERT INTO utilities VALUES ('{}','{}','{}','{}','{}','{}')""".format(
            utObject.id, utObject.licensePlate, utObject.year, utObject.weight,
            utObject.maintenance, utObject.type
        ))
        connection.commit()

def queryVehiclesGeneral():

    global cursor

    print("Cars:")
    cursor.execute("""SELECT * FROM cars""")
    rows = cursor.fetchall()

    for carInfo in rows:
        print(carInfo)

    print("Trucks:")
    cursor.execute("""SELECT * FROM trucks""")
    rows = cursor.fetchall()

    for truckInfo in rows:
        print(truckInfo)

    print("Utility Vehicles:")

    cursor.execute("""SELECT * FROM utilities""")
    rows = cursor.fetchall()

    for utInfo in rows:
        print(utInfo)

def queryVehicleSpecific():

    global cursor

    idNumber = int(input("Insert vehicles ID to query information: "))

    vehicle = None

    cursor.execute("""SELECT * FROM cars WHERE id = '{}'
                    UNION
                    SELECT * FROM trucks WHERE id = '{}'
                    UNION
                    SELECT * FROM utilities WHERE id = '{}'""".format(idNumber, idNumber, idNumber))
    row = cursor.fetchall()
    vehicle = row
    print(vehicle)

