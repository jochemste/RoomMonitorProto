import http.server
import socketserver

class HttpServerProxy():
    def __init__(self, hostaddress, port):
        self.handler = http.server.SimpleHTTPRequestHandler
        self.hostaddress = hostaddress
        self.port = port
        self.httpd = socketserver.TCPServer((self.hostaddress, self.port), self.handler)
        self.data = {"data": "Not available"}
        self.writeToHtml(self.data)

    def writeToHtml(self, data_dict):
        if not data_dict == self.data:
            with open("index.html", "w") as fd:
                data = [f'{key}: {value}\n' for key, value in data_dict.items()]
                for line in data:
                    fd.write(line)
            self.data = data_dict

    def provide(self, data_dict):
        self.writeToHtml(data_dict)

    def start(self):
        self.httpd.serve_forever()

    def stop(self):
        self.httpd.shutdown()
        
