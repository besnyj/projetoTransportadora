from vehiclesParent import Vehicles

class Cars(Vehicles):
    def __init__(self, id, licensePlate, year, weight, maintenance, mileage):
        super(Cars, self).__init__(id, licensePlate, year, weight, maintenance)
        self.mileage = mileage