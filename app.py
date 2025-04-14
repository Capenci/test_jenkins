from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello, World! 5"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), HelloHandler)
    print("Serving on port 8000")
    server.serve_forever()
