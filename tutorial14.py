'''tutorial 14:
redirect and errors'''
from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
    '''executing log in'''
    return render_template('session.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    '''
    checking if we have right method and
      then sending to success function
    '''
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success() -> str:
    '''
    returns string messaging that everything is right
    '''
    return 'logged in succesfully'

if __name__ == '__main__':
    app.run(debug=True)
