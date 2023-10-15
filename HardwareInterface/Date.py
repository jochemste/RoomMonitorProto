from .ISensor import ISensor

from datetime import datetime

class DateProxy(ISensor):
    def __init__(self):
        super(DateProxy, self).__init__()

    def read(self):
        self.data_dict["timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return super(DateProxy, self).read()
