from flask import Flask

app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/start')
def start():
    return 'Start'


@app.route('/stop')
def stop():
    return "Stop"
