import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import request

HOSTNAME = "localhost"
PORT = 8080


def open_db():
    db = sqlite3.connect("src/database.db")
    cur = db.cursor()
    return db, cur


class WebServer(BaseHTTPRequestHandler):

    def request_type(self):
        args = self.path.split("/")[1:]
        if len(args) > 0:
            db, cur = open_db()
            if args[0] == "user":
                pass
            elif args[0] == "layout":
                pass
            else:
                pass

    def do_GET(self):
        self.request_type()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(f'{{"{self.path}": true}}', "utf-8"))


if __name__ == "__main__":
    server = HTTPServer((HOSTNAME, PORT), WebServer)
    print(f"Server started @ http://{HOSTNAME}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()