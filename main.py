from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def sign():
    return render_template('sign.html', username='', username_error='',
        password='', password_error='', c_password='',
        email='', email_error='')

@app.route("/", methods=['POST'])
def validate_sign():

    username = request.form[ 'username' ]
    password = request.form['password']
    c_password = request.form['c_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''

    if 3 > len(username) > 20:
        username_error = 'Must be between 3 to 20 charcters'
        
    for char in username:
        if char == ' ':
            username_error= 'No space in username'

    if 3 > len(password) > 20:
        password_error= 'Must be between 3 to 20 charcters'       

    for char in password:
        if char == ' ':
            password_error= 'No space in password'
            password = ''
            c_password = ''

    if password != c_password:
        password_error = 'Passwords do not match'
        password = ''
        c_password = ''
 
    check1 = 'n'
    check2 = 'n'

    if email != '':
        for char in email:
            if char == ' ':
                email_error = 'No space in Email'
            elif char == '@':
                check1 = 'y'
            elif char == '.':
                check2 = 'y'
            elif check1 == 'n' or check2 == 'n':
                email_error = 'Email must contain "@" and "." to be valid'
            else:
                email_error = ''

    if username_error == '' and password_error == '' and email_error == '':
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('sign.html', password_error=password_error,
            username_error=username_error, email_error=email_error,
            username=username, password=password,
            c_password=c_password, email=email)

@app.route('/welcome')
def welcome_user():
    user = request.args.get('username')
    return '<h1>Welcome {0}!</h1>'.format(user)


app.run()    