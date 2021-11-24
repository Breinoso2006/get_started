#import flask
from os import environ, name
from flask import Flask, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/')
def index():
    return 'index'

def test():
    return 'test with add url rule'

app.add_url_rule('/test','test', test)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/admin')
def admin():
    return '<h1>Admin</h1>'

@app.route('/guest/<guest>')
def guest(guest):
    return '<h1>Guest:'+guest+ '</h1>'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest = name))
