import seeed_dht

class HardwareInterface():
    def __init__(self):
        # Set dht11 as temperature sensor
        self.sensor = {}
        self.sensor["temperature"] = seeed_dht.DHT("11", 12)
        self.sensor["humidity"] = self.sensor["temperature"]
        
    def readTemperature(self):
        _, temp = self.sensor["temperature"].read()
        return temp

    def readHumidity(self):
        humi, _ = self.sensor["humidity"].read()
        return humi

    def read(self):
        data_dict = {}
        data_dict["temperature"] = self.readTemperature()
        data_dict["humidity"] = self.readHumidity()
        return data_dict
