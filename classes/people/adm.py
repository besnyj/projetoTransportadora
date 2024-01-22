from workers import Workers


class Administrator(Workers):
    def __init__(self):
        super().__init__()
        self.department = None
