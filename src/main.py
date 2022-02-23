from enum import Enum
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Literal
import json

HOSTNAME = "localhost"
PORT = 8080


def open_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    db = sqlite3.connect("src/database.db")
    cur = db.cursor()
    return db, cur


def close_db(db: sqlite3.Connection) -> None:
    db.commit()
    db.close()


def format_as_json(items: list) -> str:
    return json.dumps({"response": [item[0] for item in items]})


class ResponseType(Enum):
    UNKNOWN = 1
    USER = 2
    LAYOUT = 3


class WebServer(BaseHTTPRequestHandler):

    def determine_type(self) -> ResponseType:
        self.request_args = self.path.split("/")[1:]
        if len(self.request_args) > 0:
            if self.request_args[0][:4] == "user":
                return ResponseType.USER
            elif self.request_args[0] == "layout":
                return ResponseType.LAYOUT
        return ResponseType.UNKNOWN

    def layout_GET(self) -> tuple[Literal[200, 404], str]:
        db, cur = open_db()
        if len(self.request_args) > 1:
            cur.execute("SELECT layout_ID FROM layouts WHERE name = ?",
                        (self.request_args[1], ))
            found_ID = cur.fetchone()
            if found_ID:
                cur.execute("SELECT data FROM content WHERE layout_ID = ?",
                            (found_ID[0], ))
                found_data = cur.fetchone()
                close_db(db)
                return 200, format_as_json((found_data, ))
            else:
                close_db(db)
                return 404, ""
        else:
            cur.execute("SELECT name FROM layouts")
            found_data = format_as_json(cur.fetchall())
            close_db(db)
            return 200, found_data

    def user_GET(self) -> tuple[Literal[200, 404], str]:
        if "?" and "&" in self.request_args[0]:
            user = [
                i[3:] for i in self.request_args[0].split("?")[1].split("&")
            ]
            print(user)
            if len(user) == 2:
                db, cur = open_db()
                cur.execute("SELECT password FROM users WHERE username = ?",
                            (user[0], ))
                found_password = cur.fetchone()
                print(found_password)
                close_db(db)
                if found_password:
                    if found_password[0] == user[1]:
                        print("here")
                        return 200, format_as_json((["true"], ))
                return 200, format_as_json((["false"], ))
        return 404, ""

    def do_GET(self) -> None:
        type = self.determine_type()
        if type == ResponseType.UNKNOWN:
            print(f"Response 404")
            self.send_response(400)
            self.end_headers()
        elif type == ResponseType.LAYOUT:
            code, response = self.layout_GET()
            print(f"Response LAYOUT {code} {response}")
            self.send_response(code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if code == 200:
                self.wfile.write(bytes(response, "utf-8"))
        elif type == ResponseType.USER:
            code, response = self.user_GET()
            print(f"Response USER {code} {response}")
            self.send_response(code)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            if code == 200:
                self.wfile.write(bytes(response, "utf-8"))


if __name__ == "__main__":
    server = HTTPServer((HOSTNAME, PORT), WebServer)
    print(f"Server started @ http://{HOSTNAME}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer closing")
        server.server_close()