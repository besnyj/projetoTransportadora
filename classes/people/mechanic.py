from workers import Workers


class Mechanic(Workers):
    def __init__(self):
        super().__init__()
        self.tools = None
        self.maintenanceHistory = None
        self.trucksAssigned = None
