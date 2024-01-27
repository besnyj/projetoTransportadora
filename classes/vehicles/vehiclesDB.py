import sqlite3
from classes.vehicles.cars import Cars
from classes.vehicles.trucks import Trucks
from classes.vehicles.utilities import Utilities


def insertVehicles():

    connection = sqlite3.connect("vehiclesDB.db")
    cursor = connection.cursor()

    print("Add new vehicle: \n1. Car \n2. Trucks \n3. Utility")


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

    connection.close()

def queryVehiclesGeneral():

    connection = sqlite3.connect("vehiclesDB.db")
    cursor = connection.cursor()

    cursor.execute("""SELECT * FROM cars UNION SELECT * FROM trucks UNION SELECT * FROM utilities""")
    results = cursor.fetchall()

    resultsList = []

    for vehicles in results:

        resultsDict = {
            'id': vehicles[0],
            'licensePlate': vehicles[1],
            'year': vehicles[2],
            'weight': vehicles[3],
            'maintenance': vehicles[4],
            'mileage': vehicles[5]
        }

        resultsList.append(resultsDict)



    return resultsList

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

def deleteVehicle():

    connection = sqlite3.connect("vehiclesDB.db")
    cursor = connection.cursor()

    idNumber = int(input("Insert vehicle's ID to delete from DB: "))

    cursor.execute("""DELETE FROM cars WHERE id = '{}'""".format(idNumber))
    connection.commit()
    cursor.execute("""DELETE FROM trucks WHERE id = '{}'""".format(idNumber))
    connection.commit()
    cursor.execute("""DELETE FROM utilities WHERE id = '{}'""".format(idNumber))
    connection.commit()

    print(f'Vehicle with ID {idNumber} has been deleted from the DB')

    connection.close()

def updateVehicleInfo():

    connection = sqlite3.connect("vehiclesDB.db")
    cursor = connection.cursor()

    idNumber = int(input("Insert vehicle's ID to update information"))

    licensePlate = input("License Plate: ")
    year = input("Year: ")
    weight = int(input("Weight: "))
    maintenance = input("Maintenance: ")
    extra = input("Mileage, Trip History or Type: ")

    cursor.execute("""UPDATE cars SET licensePlate='{}', year='{}',
     weight='{}', maintenance='{}', mileage='{}' WHERE id = '{}'""".format(
        licensePlate, year, weight, maintenance, extra, idNumber
    ))

    connection.commit()

    print(f'Information for Vehicle with ID {idNumber} have been updated: ')

    connection.close()

