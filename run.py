from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)

app.secret_key = b'123456789'


@app.route('/')
def index():
    context = [
        ['task 7', 'power_get'],
        ['task 8', 'flash_get'],
        ['task 9', 'cookie_get']
    ]
    return render_template('about.html', context=context)


# task 7
@app.get('/power')
def power_get():
    context = {
        "title": "Task 7 - Power",
        "task": '''Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить". При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.'''
    }
    return render_template('power_t07.html', **context)


@app.post('/power')
def power_post():
    number = request.form['number']
    try:
        number = int(number)
    except ValueError as e:
        return f'Your input can not be transform to integer number: {number}.<br>Error: {e}', 400
    return f'Your number was {number}.<br>Square of this number: {number ** 2}', 200


# task 8
@app.get('/flash')
def flash_get():
    context = {
        "title": "Task 8",
        "task": '''Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить". При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".'''
    }
    return render_template('flash_form.html', **context)


@app.post('/flash')
def flash_post():
    name = request.form.get('name')
    if not name:
        flash(message='Please enter your name', category='danger')
        return redirect(url_for('flash_get'))
    flash(message='Hello, {}!'.format(name), category='success')
    return redirect(url_for('flash_get'))


# task9
@app.get('/cookie')
def cookie_get():
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
