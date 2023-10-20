#!/usr/bin/python3
'''Starts a Flask web application:
    - must be listening on 0.0.0.0 and port 5000
    - route '/' must display "Hello HBNB!"
    - route '/hbnb' must display "HBNB!"
    - must use the option 'strict_slashes=False' in your route definition
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''returns "Hello HBNB!" for the route '/'
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''returns "HBNB" for the route '/hbnb'
    '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
