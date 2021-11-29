from flask import Flask, json, render_template, request, abort, make_response, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from json import dumps

app = Flask(__name__, static_folder='templates/css', template_folder='templates')
app.secret_key = "123456"


#Criando rotas
@app.route('/')
def index():
    return render_template('index.html')

#Construção de url
def test():
    return 'test with add url rule'

app.add_url_rule('/test','test', test)

#Url dinâmicas e arquivos estáticos
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

#Métodos HTTP
@app.route('/add', methods=["GET","POST"])
def add():
    if request.method == "POST":
        return dumps(request.form)
    elif request.method == "GET":
        return "GET METHOD"

#Objetos de Requisição
@app.route('/index', methods=["GET","POST"])
def index2():
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([t1, t2])

#Redirecionamento e erros
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/status', methods=["GET","POST"])
def login_status():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('sucess'), code=200) #302 para ir direto
        else:
            abort(401)
    else:
        abort(403)

@app.route('/sucess')
def sucess():
    return 'Sucess'

#Templates com jinja2
@app.route('/jinja')
def jinja():
    x = 2
    y = 4
    query = request.args.to_dict()
    return render_template('jinja.html', valorx = x, valory = y, query = query)

#Enviando dados para/entre templates
@app.route('/notas')
def notas():
    return render_template('notas.html')

@app.route('/calculo', methods=['POST'])
def calculo():
    total = sum([int(v) for v in request.form.to_dict().values()])
    return render_template('calculo.html', total = total)

#Cookies
@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    if request.method == "POST":
        dados = request.form['c']
    
    resp = make_response(render_template('setcookie.html'))
    resp.set_cookie('testeCookie', dados)

    return resp

@app.route('/getcookie')
def getcookie():
    cookie_name = request.cookies.get('testecookie')

    return '<h1>Valor cookie é: {}</h1>'.format(cookie_name)

#Session
@app.route('/session')
def sessionn():
    username = ''
    if 'username' in session:
        username = session['username']
    return render_template('session.html', username=username)

@app.route('/sessionlogin', methods=["GET","POST"])
def sessionlogin():
    if request.method == "POST" and request.form['username'] != '':
        session['username'] = request.form['username']
        return redirect(url_for('sessionn'))
    return render_template('sessionlogin.html')

@app.route('/sessionlogout')
def sessionlogout():
    session.pop('username', None)
    return redirect(url_for('sessionn'))

@app.route('/sessiontest/<s>')
def sessiontest(s):
    session['username'] = s
    return redirect(url_for('sessionn'))