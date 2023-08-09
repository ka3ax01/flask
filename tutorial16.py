from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('upload'))
@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET','POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded succesfully'

if __name__ == '__main__':
    app.run(debug=True)