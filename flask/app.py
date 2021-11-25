from flask import Flask, json, render_template, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from json import dumps

app = Flask(__name__, static_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

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
    return '<h1>Guest:' + guest + '</h1>'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest = name))

@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == "POST":
        return dumps(request.form)
    elif request.method == "GET":
        return "GET MEHOD"

@app.route('/index', methods=["GET","POST"])
def index2():
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([t1, t2])