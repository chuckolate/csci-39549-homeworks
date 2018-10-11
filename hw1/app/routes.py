from app import app
from flask import render_template

@app.route('/')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/subtract')
def subtract():
    return render_template('subtract.html')

@app.route('/multiply')
def multiply():
    return render_template('multiply.html')

@app.route('/divide')
def divide():
    return render_template('divide.html')