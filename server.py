from flask import Flask, redirect, session, render_template, request
import re
app = Flask(__name__)
app.secret_key = "I<3SecretsToo"
EMailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
@app.route('/')
def main():
	return render_template('main.html')

@app.route('/process', methods = ['POST'])
def validate():
	del session['errors']
	if request.form['fname'] == "":
		session['errors'] = {"fname": "The first name field is required"}
	elif not str.isalpha(request.form['fname']):
		session['errors'] = {"fname": "First name cannot have number or symbols"}
	if request.form['lname'] == "":
		session['errors'] = {"lname": "The last name field is required"}
	elif not str.isalpha(request.form['fname']):
		session['errors'] = {"lname": "Last name cannot have number or symbols"}
	if not EMailRegex.match(request.form['email']):
		session['errors'] = {"email": "The E-Mail must be a valid e-mail address"}
	if request.form['password'] == "":
		session['errors'] = {"password": "The password field is required"}
	elif len(request.form['password']) < 8:
		session['errors'] = {"password": "Password must be at least 8 characters"}
	elif not any(char.isdigit() for char in request.form['password']):
		session['errors'] = {"password": "Password must contain at least one number"}
	elif not any(char.isupper() for char in request.form['password']):
		session['errors'] = {"password": "Password must contain at least one uppercase letter"}
	if request.form['confirmpass'] != request.form['confirmpass']:
		session['errors'] = {"confirmpass": "The confirmation does not match the password"}
	if session['errors']:
		return redirect('/')
	else:
		return render_template('thanks.html')

	