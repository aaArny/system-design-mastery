from flask import Flask, jsonify 
import os, socket 

app = Flask(__name__)


@app.route('/')
def index():
  return jsonify({
    "service": os.environ.get('SERVICE_NAME', 'unknown'),
    "hostname": socket.gethostname(),
    "message": "Hello from the reverse proxy!"
  })

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)