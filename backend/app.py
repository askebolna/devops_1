from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080
RESPONSE_TEXT = "Hello from Effective Mobile!"

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(RESPONSE_TEXT.encode('utf-8'))

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', PORT), SimpleHandler)
    print(f"Server started on port {PORT}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
