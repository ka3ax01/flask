from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method=='POST':
        resul = request.form
        return render_template("table.html", result=resul)
if __name__ == '__main__':
    app.run(debug=True)
