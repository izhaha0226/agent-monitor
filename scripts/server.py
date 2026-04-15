from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path('/Users/yosiki/projects/agent-monitor')
INDEX = (ROOT / 'index.html').read_bytes()
FAVICON = b''
ROBOTS = b'User-agent: *\nAllow: /\n'

class Handler(BaseHTTPRequestHandler):
    server_version = 'AgentMonitorHTTP/1.0'

    def _send(self, status: int, body: bytes, content_type: str):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(body)

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        if self.path in ['/', '/index.html', '']:
            return self._send(200, INDEX, 'text/html; charset=utf-8')
        if self.path == '/favicon.ico':
            return self._send(204, FAVICON, 'image/x-icon')
        if self.path == '/robots.txt':
            return self._send(200, ROBOTS, 'text/plain; charset=utf-8')
        if self.path == '/health':
            return self._send(200, b'{"ok":true}', 'application/json')
        return self._send(404, b'Not Found', 'text/plain; charset=utf-8')

    def log_message(self, fmt, *args):
        print('%s - - [%s] %s' % (self.address_string(), self.log_date_time_string(), fmt % args), flush=True)

if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 1188), Handler)
    server.serve_forever()
