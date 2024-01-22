from workers import Workers


class Drivers(Workers):
    def __init__(self):
        super().__init__()
        self.hireTime = None
        self.truck = None
        self.licenses = None
        self.tripHistory = None
