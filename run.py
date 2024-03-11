from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)


@app.route('/')
def index():
    context = [
        ['task 7', 'power'],
        ['task 8', 'flash'],
        ['task 9', 'cookie']
    ]
    return render_template('about.html', context=context)


# task 7
@app.get('/power')
def power():
    pass


@app.get('/flash')
def flash():
    pass


# task9
@app.get('/cookie')
def cookie():
    pass


@app.get('/login')
def login_get():
    return render_template('username_form.html')


@app.post('/login')
def login_post():
    test_data = {
        'username': 'user1',
        'password': '1234'
    }
    username = request.form['username']
    password = request.form['password']

    if username == test_data['username'] and password == test_data['password']:
        return 'Success', 200
    else:
        return 'Fail', 503


if __name__ == '__main__':
    app.run(debug=True)
