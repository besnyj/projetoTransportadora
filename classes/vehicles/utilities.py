from vehiclesParent import Vehicles

class Utilities(Vehicles):
    def __init__(self, id, licensePlate, year, weight, maintenance, type):
        super(Utilities, self).__init__(id, licensePlate, year, weight, maintenance)
        self.type = type