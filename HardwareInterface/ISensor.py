class ISensor():
    def __init__(self):
        self.activated = False
        self.data_dict = {}

    def read(self):
        return self.data_dict
