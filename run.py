from flask import Flask, render_template, request, flash, redirect, url_for, session
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)

app.secret_key = b'123456789'


@app.route('/')
def index():
    context = {'tasks': [
        ['task 7', 'power_get'],
        ['task 8', 'flash_get'],
        ['task 9', 'login_get']],
        'title': 'Main page'
    }
    if 'username' in session:
        context['username'] = session['username']
        context['email'] = session['email']
    return render_template('about.html', **context)


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
        "title": "Task 8 - Flash",
        "task": '''Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить".<br>При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".'''
    }
    return render_template('flash_form_t08.html', **context)


@app.post('/flash')
def flash_post():
    name = request.form.get('name')
    if not name:
        flash(message='Please enter your name', category='danger')
        return redirect(url_for('flash_get'))
    flash(message='Hello, {}!'.format(name), category='success')
    return redirect(url_for('flash_get'))


# task9
@app.get('/login')
def login_get():
    context = {
        "title": "Task 9 - Cookie",
        "task": '''Создать страницу, на которой будет форма для ввода имени
    и электронной почты.<br>
    При отправке которой будет создан cookie файл с данными
    пользователя<br>
    Также будет произведено перенаправление на страницу
    приветствия, где будет отображаться имя пользователя.<br>
    На странице приветствия должна быть кнопка "Выйти"<br>
    При нажатии на кнопку будет удален cookie файл с данными
    пользователя и произведено перенаправление на страницу
    ввода имени и электронной почты.'''
    }
    return render_template('username_form_t09.html', **context)


@app.post('/login')
def login_post():
    username = request.form.get('username', default=None)
    email = request.form.get('email', default=None)

    if username:
        session['username'] = username if username else 'Unknown'
        session['email'] = email if email else 'Unknown'
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login_get'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('login_get'))


if __name__ == '__main__':
    app.run(debug=True)
