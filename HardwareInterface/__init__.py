
from .SensorTempHum import SensorTempHumProxy
from .Date import DateProxy

class HardwareInterface():
    def __init__(self):
        self.hardware = []
        self.addHardware(SensorTempHumProxy())
        self.addHardware(DateProxy())
        
    def addHardware(self, hardware):
        self.hardware.append(hardware)

    def read(self):
        data_dict = {}
        for hardware in self.hardware:
            tmp_data_dict = hardware.read()
            for k,v in tmp_data_dict.items():
                data_dict[k] = v
                
        return data_dict
