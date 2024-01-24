from vehiclesParent import Vehicles

class Trucks(Vehicles):
    def __init__(self):
        super().__init__()
        self.tripHistory = None