from .ISensor import ISensor

import time
import seeed_dht

class SensorTempHumProxy(ISensor):
    def __init__(self):
        # Set sensor as DHT11
        self.sensor = seeed_dht.DHT("11", 12)
        self.required_read_delay = 1 # seconds
        super(SensorTempHumProxy, self).__init__()

    def read(self):
        self.data_dict["humidity"], self.data_dict["temperature"] = self.sensor.read()
        time.sleep(self.required_read_delay)
        return super(SensorTempHumProxy, self).read()
