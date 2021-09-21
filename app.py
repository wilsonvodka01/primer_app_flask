from flask import Flask
from flask import Request

app = Flask(__name__)

@app.route('/')
def index():
  return 'hola mundo'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<last_name>')
def params (name = 'volor por defecto', last_name = 'sin apellido'):
  return 'el parametro es : {} {}'.format(name, last_name)

if __name__ == '__main__':
  app.run(debug = True, port= 8050)  