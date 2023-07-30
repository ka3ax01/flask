from flask import Flask

app = Flask(__name__)
def index() ->str:
  str="""
  <html>
  <body>
  <h1>Hello World</h1>
  </body>
  </html>
  """
  return str

if __name__ == '__main__':
  app.run(debug=True)
