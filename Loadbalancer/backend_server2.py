# backend_server.py
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health_check():
    return '', 200

@app.route('/')
def index():
    return 'Hello from Backend Server!'

if __name__ == '__main__':
    app.run(port=8002)
