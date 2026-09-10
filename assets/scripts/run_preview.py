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
import html
import json
import re
import secrets
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
    values = {}
    for pair in subs:
        if "=" not in pair:
            raise ValueError("替换参数必须使用 KEY=VALUE")
        key, value = pair.split("=", 1)
        key = key.strip()
        if not re.fullmatch(r"[A-Z_]+", key):
            raise ValueError("无效替换参数")
        if key.startswith("CITY_") and key != "CITY_NAME" and not re.fullmatch(r"#[0-9a-fA-F]{3,8}|rgba?\([0-9.,% ]+\)", value):
            raise ValueError("颜色必须是十六进制或 rgb/rgba 数值")
        if key == "RECEIVER_PORT" and not (value.isdigit() and 0 < int(value) < 65536):
            raise ValueError("端口必须在 1–65535")
        if key == "LANG" and value not in {"zh", "en"}:
            raise ValueError("LANG 仅支持 zh/en")
        values[key] = value
    # 同一占位符在 HTML 文本与 JS 字符串中出现，分别编码；不逐次替换用户值中的占位符。
    parts = re.split(r"(<script\b[^>]*>.*?</script\s*>)", text, flags=re.I | re.S)
    for i, part in enumerate(parts):
        is_script = bool(re.match(r"<script\b", part, re.I))
        def replacement(match):
            value = values.get(match[1])
            if value is None:
                return match[0]
            if is_script:
                encoded = json.dumps(value, ensure_ascii=True)[1:-1]
                return encoded.replace("'", "\\u0027").replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            return html.escape(value, quote=True)
        parts[i] = re.sub(r"__([A-Z_]+)__", replacement, part)
    Path(output_path).write_text("".join(parts), encoding="utf-8")


def make_handler(html_path, result_path, token):
    """仅接受当前预览页面携带会话令牌的 JSON 提交。"""
    class Handler(BaseHTTPRequestHandler):
        def allowed_host(self):
            port = self.server.server_port
            return self.headers.get("Host") in {f"localhost:{port}", f"127.0.0.1:{port}"}

        def do_GET(self):
            if not self.allowed_host():
                self.send_error(403); return
            if self.path != "/":
                self.send_error(404); return
            body = Path(html_path).read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers(); self.wfile.write(body)

        def do_POST(self):
            port = self.server.server_port
            origin = self.headers.get("Origin")
            if (not self.allowed_host() or origin not in {f"http://localhost:{port}", f"http://127.0.0.1:{port}"}
                    or not secrets.compare_digest(self.headers.get("X-Citycraft-Token", ""), token)):
                self.send_error(403); return
            if self.path != "/submit":
                self.send_error(404); return
            if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                self.send_error(415); return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 16384:
                    raise ValueError()
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict) or not data:
                    raise ValueError()
            except (ValueError, UnicodeDecodeError):
                self.send_error(400); return
            with self.server.submission_lock:
                if self.server.submitted:
                    self.send_error(409); return
                Path(result_path).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
                self.server.submitted = True
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers(); self.wfile.write(b'{"ok":true}')
    return Handler


def main():
    args = parse_args()

    if not 0 < args.port < 65536 or args.timeout <= 0:
        raise ValueError("端口或超时无效")
    token = secrets.token_hex(32)
    result_path = Path(args.result) if args.result else Path(tempfile.gettempdir()) / ("citycraft-" + secrets.token_hex(16) + ".json")
    if result_path.exists() or Path(args.output).exists():
        raise FileExistsError("输出已存在，请使用新的 output/result 路径")

    # 1. Fill template
    substitute(args.template, args.output, args.subs + ["SESSION_TOKEN=" + token])

    # 2. Start HTTP server
    html_abs = str(Path(args.output).resolve())
    Handler = make_handler(html_abs, str(result_path), token)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    server.submission_lock = threading.Lock()
    server.submitted = False
    threading.Thread(target=server.serve_forever, daemon=True).start()

    # 3. Open browser (cross-platform: macOS / Linux / Windows)
    webbrowser.open("http://localhost:{port}".format(port=args.port))

    # 4. Poll for result
    for _ in range(args.timeout):
        if server.submitted:
            data = result_path.read_text(encoding="utf-8")
            try:
                result_path.unlink()
            except OSError:
                pass
            server.shutdown()
            server.server_close()
            print(data)
            return
        time.sleep(1)

    # Timeout
    server.shutdown()
    server.server_close()
    sys.stderr.write(
        "No submission in {t}s. Ask the user to type their choice manually.\n"
        .format(t=args.timeout)
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
