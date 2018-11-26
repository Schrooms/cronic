from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/start')
def start():
    return 'start'


@app.route('/stop')
def stop():
    return "Stop"
