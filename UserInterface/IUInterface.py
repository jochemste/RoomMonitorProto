class IUInterface():
    def __init__(self):
        self.running = False
        self.data = {"data": "Not available"}

    def provide(self, data_dict):
        pass
        
    def start(self):
        self.running = True

    def stop(self):
        self.running = False
