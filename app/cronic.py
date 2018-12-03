from flask import Flask
from flask import render_template

app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def index():
    return render_template('index.html', name='Index Page')


@app.route('/start', methods=['GET', 'POST'])
def start():
    return 'Start'


@app.route('/stop', methods=['GET', 'POST'])
def stop():
    return "Stop"
