from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World!"

@app.route('/time')
def get_time():
    return f"Current server time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
