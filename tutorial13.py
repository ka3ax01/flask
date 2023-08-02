import secrets
import string
from flask import Flask, session, redirect, url_for, render_template, request
app = Flask(__name__)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

app.secret_key = generate_random_string(32)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f"Logged in as {username}<br>"+\
                "<b><a href = '/logout'> click here to log out</a></b>"
    return "You are not logged in <br><a href ='/login'><b>"+\
            "click here to log in</b></a>"

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    