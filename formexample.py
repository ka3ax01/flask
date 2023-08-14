import secrets
import string
from flask import Flask, render_template, request, flash
from form import ContactForm
app = Flask(__name__)
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

app.secret_key = generate_random_string(32)

@app.route('/contact', methods = ['GET','POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        return render_template('success.html')
    if request.method == 'GET':
        return render_template('contact.html', form = form)
    
if __name__ == '__main__':
    app.run(debug=True)