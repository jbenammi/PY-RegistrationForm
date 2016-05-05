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
	session['err_fname'] = []
	session['err_lname'] = []
	session['err_email'] = []
	session['err_password'] = []
	session['err_confirm'] = []
	sess_count = 0
	if request.form['fname'] == "":
		session['err_fname'] = "The first name field is required"
		sess_count += 1
	elif not str.isalpha(str(request.form['fname'])):
		session['err_fname'] = "First name cannot have number or symbols"
		sess_count += 1
	if request.form['lname'] == "":
		session['err_lname'] = "The last name field is required"
		sess_count += 1
	elif not str.isalpha(str(request.form['lname'])):
		session['err_lname'] = "Last name cannot have number or symbols"
		sess_count += 1
	if not EMailRegex.match(request.form['email']):
		session['err_email'] = "The E-Mail must be a valid e-mail address"
		sess_count += 1
	if len(request.form['password']) < 8:
		session['err_password'] = "Password must be at least 8 characters"
		sess_count += 1
	elif not any(char.isdigit() for char in str(request.form['password'])):
		session['err_password'] = "Password must contain at least one number"
		sess_count += 1
	elif not any(char.isupper() for char in str(request.form['password'])):
		session['err_password'] = "Password must contain at least one uppercase letter"
		sess_count += 1
	if request.form['confirmpass'] != request.form['password']:
		session['err_confirm'] = "The confirmation does not match the password"
		sess_count += 1
	if sess_count > 0:
		return redirect('/')
	else:
		del session['err_fname']
		del session['err_lname']
		del session['err_email']
		del session['err_password']
		del session['err_confirm']
		return render_template('thanks.html')

@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')
app.run(debug=True)

	