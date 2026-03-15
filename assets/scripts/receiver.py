"""
One-shot HTTP server for citycraft localhost bridge.

Serves options-preview.html at GET /
Receives the user's selection via POST /submit → writes /tmp/citycraft_selection.json → shuts down

Usage:
  python3 receiver.py [port] [html_path] [output_path]

Defaults:
  port        17432
  html_path   ./options-preview.html
  output_path /tmp/citycraft_selection.json
"""

import sys
import threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path

PORT        = int(sys.argv[1])  if len(sys.argv) > 1 else 17432
HTML_PATH   = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("options-preview.html")
OUTPUT_PATH = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("/tmp/citycraft_selection.json")


class Handler(BaseHTTPRequestHandler):

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path != "/":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        body = HTML_PATH.read_bytes()
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/submit":
            self.send_response(404)
            self._cors()
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        OUTPUT_PATH.write_bytes(body)
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')
        threading.Thread(target=self.server.shutdown, daemon=True).start()

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    server.serve_forever()
