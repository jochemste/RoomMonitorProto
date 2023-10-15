from .HttpServer import HttpServerProxy

from threading import Thread

class UserInterface():
    def __init__(self):
        self.interfaces = []
        self.threads = []

        self.addInterface(HttpServerProxy("", 8000))

    def provide(self, data_dict):
        for iface in self.interfaces:
            iface.provide(data_dict)

    def addInterface(self, interface):
        self.interfaces.append(interface)
        self.threads.append(Thread(target=interface.start))
        self.threads[-1].start()

    def stop(self):
        for iface in self.interfaces:
            iface.stop()
        for thread in self.threads:
            thread.join()        
