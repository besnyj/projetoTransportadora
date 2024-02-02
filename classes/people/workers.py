from peopleParent import People


class Workers(People):
    def __init__(self):
        super().__init__()
        self.role = None
        self.salary = None