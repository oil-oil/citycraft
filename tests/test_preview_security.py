import http.client
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import threading
import unittest
sys.path.insert(0, str(Path(__file__).parents[1] / 'assets/scripts'))
import run_preview as preview

class PreviewTests(unittest.TestCase):
    def test_real_templates_escape_product_and_keep_city_selection(self):
        root = Path(__file__).parents[1]
        malicious = "O'Reilly </script><script>throw 1</script> __CITY_NAME__"
        with tempfile.TemporaryDirectory() as tmp:
            for template in root.glob('assets/*preview-template.html'):
                out = Path(tmp) / template.name
                preview.substitute(template, out, ['PRODUCT_NAME=' + malicious, 'PRODUCT_HEADLINE=' + malicious, 'CITY_NAME=Kyoto', 'LANG=zh', 'SESSION_TOKEN=fake-test-session'])
                text = out.read_text()
                self.assertNotIn("<script>throw 1</script>", text)
                for i, script in enumerate(re.findall(r'<script[^>]*>(.*?)</script>', text, re.S)):
                    js = Path(tmp) / f'{i}.js';js.write_text(script)
                    result = subprocess.run(['node', '--check', str(js)], capture_output=True)
                    self.assertEqual(result.returncode, 0, result.stderr)
                if 'options-' in template.name:
                    script = re.search(r"const CITY = (.*);", text)[1]
                    result = subprocess.run(['node', '-e', 'process.stdout.write(' + script + ')'], capture_output=True, text=True)
                    self.assertEqual(result.stdout, 'Kyoto')

    def test_cross_origin_and_missing_token_cannot_submit(self):
        with tempfile.TemporaryDirectory() as tmp:
            html = Path(tmp)/'page.html';html.write_text('preview')
            out = Path(tmp)/'result.json'
            server = preview.ThreadingHTTPServer(('127.0.0.1', 0), preview.make_handler(html, out, 'test-session'))
            server.submission_lock = threading.Lock();server.submitted = False
            threading.Thread(target=server.serve_forever, daemon=True).start()
            try:
                port = server.server_port
                def post(origin, token, body='{"city":"Kyoto"}'):
                    conn = http.client.HTTPConnection('127.0.0.1', port, timeout=2)
                    conn.request('POST', '/submit', body, {'Origin': origin, 'X-Citycraft-Token':token, 'Content-Type':'application/json'})
                    response = conn.getresponse();status=response.status;response.read();conn.close();return status
                self.assertEqual(post('https://untrusted.example', 'test-session'),403)
                self.assertEqual(post(f'http://127.0.0.1:{port}', ''),403)
                self.assertFalse(out.exists())
                self.assertEqual(post(f'http://127.0.0.1:{port}', 'test-session', '[]'),400)
                self.assertEqual(post(f'http://127.0.0.1:{port}', 'test-session'),200)
                self.assertEqual(json.loads(out.read_text()),{'city':'Kyoto'})
                self.assertEqual(post(f'http://127.0.0.1:{port}', 'test-session'),409)
            finally:server.shutdown();server.server_close()

    def test_css_values_cannot_escape_style(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'template.html';source.write_text('<style>:root{--bg:__CITY_BG__;}</style>')
            with self.assertRaises(ValueError):preview.substitute(source,Path(tmp)/'out.html',['CITY_BG=red;}</style><script>1</script>'])

if __name__ == '__main__':unittest.main()
