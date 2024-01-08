# import http.server
# import socketserver
# import threading
# import requests
# import time

# # Backend servers with their health check paths
# BACKEND_SERVERS = [
#     {'host': 'localhost', 'port': 8001, 'health_check': '/health'},
#     {'host': 'localhost', 'port': 8002, 'health_check': '/health'},
# ]

# class HealthCheckThread(threading.Thread):
#     def __init__(self, backend):
#         super().__init__()
#         self.backend = backend
#         self.is_healthy = True

#     def run(self):
#         while True:
#             try:
#                 response = requests.get(f"http://{self.backend['host']}:{self.backend['port']}{self.backend['health_check']}")
#                 self.is_healthy = response.status_code == 200
#             except requests.ConnectionError:
#                 self.is_healthy = False

#             time.sleep(5)

# class LoadBalancerHandler(http.server.BaseHTTPRequestHandler):
#     def do_GET(self):
#         backend = self.get_next_backend()
#         if backend is not None:
#             self.proxy_request(backend)
#         else:
#             self.send_response(503)
#             self.end_headers()
#             self.wfile.write(b'Service Unavailable')

#     def get_next_backend(self):
#         for backend in BACKEND_SERVERS:
#             if HealthCheckThread(backend).is_healthy:
#                 return backend
#         return None

#     def proxy_request(self, backend):
#         backend_host = backend['host']
#         backend_port = backend['port']
#         backend_path = self.path

#         self.send_response(200)
#         self.send_header('Content-Type', 'text/html')
#         self.end_headers()

#         with socketserver.TCPServer(("127.0.0.1", 0), http.server.SimpleHTTPRequestHandler) as httpd:
#             url = f'http://{backend_host}:{backend_port}{backend_path}'
#             self.wfile.write(requests.get(url).content)

# if __name__ == "__main__":
#     for backend in BACKEND_SERVERS:
#         HealthCheckThread(backend).start()

#     with socketserver.ThreadingTCPServer(('localhost', 8888), LoadBalancerHandler) as server:
#         print('Load balancer listening on port 8888...')
#         server.serve_forever()


from flask import Flask, request, jsonify
import random
import requests
import threading
import time

app = Flask(__name__)

# Backend servers with health check paths
BACKEND_SERVERS = [
    {'url': 'http://localhost:8001', 'health_check': '/health'},
    {'url': 'http://localhost:8002', 'health_check': '/health'},
    # Add more backend servers with their health check paths
]

class HealthCheckThread(threading.Thread):
    def __init__(self, backend):
        super().__init__()
        self.backend = backend
        self.is_healthy = True

    def run(self):
        while True:
            try:
                response = requests.get(f"{self.backend['url']}{self.backend['health_check']}")
                self.is_healthy = response.status_code == 200
            except requests.ConnectionError:
                self.is_healthy = False

            time.sleep(5)

# Start health checks for all backend servers
for backend in BACKEND_SERVERS:
    HealthCheckThread(backend).start()

@app.route('/')
def load_balance():
    healthy_backends = [backend for backend in BACKEND_SERVERS if backend['is_healthy']]
    if not healthy_backends:
        return jsonify({'error': 'No healthy backend servers available'}), 503

    selected_backend = random.choice(healthy_backends)
    return jsonify({'backend_url': selected_backend['url']})

if __name__ == '__main__':
    app.run(port=8888)
