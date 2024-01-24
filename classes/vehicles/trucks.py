from vehiclesParent import Vehicles

class Trucks(Vehicles):
    def __init__(self, id, licensePlate, year, weight, maintenance, tripHistory):
        super(Trucks, self).__init__(id, licensePlate, year, weight, maintenance)
        self.tripHistory = tripHistory