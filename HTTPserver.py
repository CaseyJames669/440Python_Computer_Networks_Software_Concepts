import socketserver

response = """HTTP/1.0 500 Internal Server Error
Content-type: text/html

Invalid Server Error"""

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """


    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.request.sendall(response)

if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
