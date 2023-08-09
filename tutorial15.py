import secrets
import string
from flask import Flask, redirect, render_template, request, url_for
from flask import flash
app = Flask(__name__)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

app.secret_key = generate_random_string(32)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    msg = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
        request.form['password'] != 'admin':
            msg = 'Invalid username or password. Please try again!'
        else:
            flash('You were succesfully logged in')
            flash('log out before log in again')
            return redirect(url_for('index'))
    return render_template('log_in.html', error=msg)

if __name__=='__main__':
    app.run(debug=True)