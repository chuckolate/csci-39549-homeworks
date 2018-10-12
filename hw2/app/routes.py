from app import app
from flask import render_template, request

@app.route('/')

@app.route('/index')
def index():
	return render_template('index.html')

# allow each endpoint to have GET and POST methods for retrieving two inputs and sending the result of the calculations
@app.route('/add', methods=['GET', 'POST'])
def add():
		if request.method == 'POST':
			num1 = request.form['num1']
			num2 = request.form['num2']
			integerResult = int(num1) + int(num2)
			return str(integerResult)
		return render_template('add.html')

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
		if request.method == 'POST':
			num1 = request.form['num1']
			num2 = request.form['num2']
			integerResult = int(num1) - int(num2)
			return str(integerResult)
		return render_template('subtract.html')

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
		if request.method == 'POST':
			num1 = request.form['num1']
			num2 = request.form['num2']
			integerResult = int(num1) * int(num2)
			return str(integerResult)
		return render_template('multiply.html')

@app.route('/divide', methods=['GET', 'POST'])
def divide():
		if request.method == 'POST':
			num1 = request.form['num1']
			num2 = request.form['num2']
			if num2 == '0':
				return 'Cannot divide by zero!'
			integerResult = int(num1) / int(num2)
			return str(integerResult)
		return render_template('divide.html')