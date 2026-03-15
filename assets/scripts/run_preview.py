#!/usr/bin/env python3
"""
run_preview.py — Cross-platform preview launcher for citycraft.

Replaces the sed + receiver.py + shell-polling combo with a single script
that works on macOS, Linux, and Windows (Python 3.6+, stdlib only).

What it does:
  1. Reads the template and substitutes __KEY__ placeholders.
  2. Writes the filled HTML to --output.
  3. Starts a one-shot HTTP server on --port (GET / → HTML, POST /submit → result).
  4. Opens the browser via webbrowser.open() (cross-platform).
  5. Blocks until POST /submit arrives or --timeout seconds elapse.
  6. Prints the submitted JSON to stdout and exits 0.
     On timeout: prints a message to stderr and exits 1.

Usage:
    python3 run_preview.py \\
        --template /path/to/template.html \\
        --output   ./preview.html \\
        --port     17433 \\
        --timeout  300 \\
        PRODUCT_NAME="My Product" \\
        PRODUCT_HEADLINE="Build faster" \\
        RECEIVER_PORT=17433

Each positional KEY=VALUE arg replaces __KEY__ in the template.
"""

import argparse
import os
import sys
import tempfile
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def parse_args():
    p = argparse.ArgumentParser(description="citycraft preview launcher")
    p.add_argument("--template", required=True, help="Path to HTML template")
    p.add_argument("--output",   required=True, help="Path to write filled HTML")
    p.add_argument("--port",     type=int, default=17432, help="HTTP port (default 17432)")
    p.add_argument("--result",   default=None,
                   help="Path to write submitted JSON (default: OS temp dir)")
    p.add_argument("--timeout",  type=int, default=300,
                   help="Seconds to wait for submission (default 300)")
    p.add_argument("subs", nargs="*",
                   help="Substitution pairs: KEY=VALUE  (replaces __KEY__ in template)")
    return p.parse_args()


def substitute(template_path, output_path, subs):
    text = Path(template_path).read_text(encoding="utf-8")
    for pair in subs:
        if "=" not in pair:
            continue
        key, _, value = pair.partition("=")
        text = text.replace("__{key}__".format(key=key.strip()), value)
    Path(output_path).write_text(text, encoding="utf-8")


def make_handler(html_path, result_path):
    """Return a BaseHTTPRequestHandler subclass bound to html_path / result_path."""

    class _Handler(BaseHTTPRequestHandler):

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
            body = Path(html_path).read_bytes()
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
            Path(result_path).write_bytes(body)
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            threading.Thread(target=self.server.shutdown, daemon=True).start()

        def log_message(self, *_):
            pass  # suppress request logs

    return _Handler


def main():
    args = parse_args()

    result_path = Path(
        args.result if args.result
        else os.path.join(tempfile.gettempdir(), "citycraft_result.json")
    )

    # Remove stale result from a previous run
    try:
        result_path.unlink()
    except OSError:
        pass

    # 1. Fill template
    substitute(args.template, args.output, args.subs)

    # 2. Start HTTP server
    html_abs = str(Path(args.output).resolve())
    Handler = make_handler(html_abs, str(result_path))
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()

    # 3. Open browser (cross-platform: macOS / Linux / Windows)
    webbrowser.open("http://localhost:{port}".format(port=args.port))

    # 4. Poll for result
    for _ in range(args.timeout):
        if result_path.exists():
            data = result_path.read_text(encoding="utf-8")
            try:
                result_path.unlink()
            except OSError:
                pass
            server.shutdown()
            print(data)
            return
        time.sleep(1)

    # Timeout
    server.shutdown()
    sys.stderr.write(
        "No submission in {t}s. Ask the user to type their choice manually.\n"
        .format(t=args.timeout)
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
