from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello from Flask App running on {socket.gethostname()}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)