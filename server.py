from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/css/'):
            try:
                filepath = self.path.lstrip('/')
                with open(filepath, 'r', encoding='utf-8') as file:
                    css_content = file.read()

                self.send_response(200)
                self.send_header('Content-type', 'text/css')
                self.end_headers()
                self.wfile.write(css_content.encode('utf-8'))

            except Exception as e:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(f'CSS file not found: {e}'.encode('utf-8'))

        elif self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()

        else:
            try:
                with open('contacts.html', 'r', encoding='utf-8') as file:
                    html_content = file.read()

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_content.encode('utf-8'))

            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f'Error: {e}'.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Received POST data:", post_data.decode('utf-8'))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Thanks for your message!</h1></body></html>")

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server started http://localhost:%s" % (8000))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server stopped.")
