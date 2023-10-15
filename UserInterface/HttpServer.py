from .IUInterface import IUInterface

import time
import http.server
import socketserver

class HttpServerProxy(IUInterface):
    def __init__(self, hostaddress, port):
        self.handler = http.server.SimpleHTTPRequestHandler
        self.hostaddress = hostaddress
        self.port = port
        self.httpd = socketserver.TCPServer((self.hostaddress, self.port), self.handler)
        self.data = {"data": "Not available"}
        self.write_interval = 30 # 2 writes per minute
        self.lastwrite = None
        self.writeToHtml(self.data)
        super(HttpServerProxy, self).__init__()

    def writeToHtml(self, data_dict):
        current_time = time.time()
        if (not data_dict == self.data) and \
           (not self.lastwrite or current_time - self.lastwrite > self.write_interval):
            with open("index.html", "w") as fd:
                data = [f'{key}: {value}\n' for key, value in data_dict.items()]
                for line in data:
                    fd.write(line)
                self.lastwrite = time.time()
            self.data = data_dict

    def provide(self, data_dict):
        self.writeToHtml(data_dict)
        super(HttpServerProxy, self).provide(data_dict)

    def start(self):
        super(HttpServerProxy, self).start()
        self.httpd.serve_forever()

    def stop(self):
        super(HttpServerProxy, self).stop()
        self.httpd.shutdown()
        
