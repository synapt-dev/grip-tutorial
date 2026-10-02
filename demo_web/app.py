import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit

from demo_core.pricing import total_cents


def handle(target: str):
    """Pure request handler: ('/price?qty=4') -> (status, json-able body)."""
    parts = urlsplit(target)
    if parts.path == "/price":
        try:
            qty = int(parse_qs(parts.query).get("qty", [""])[0])
            return 200, {"qty": qty, "cents": total_cents(qty)}
        except ValueError:
            return 400, {"error": "qty must be a non-negative integer"}
    return 404, {"error": "not found"}


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, body = handle(self.path)
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


def serve(port: int = 8080):
    HTTPServer(("127.0.0.1", port), _Handler).serve_forever()
