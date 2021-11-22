from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/newroute")
def new_route():
    return "<p>You're in a new route!<p>"

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)