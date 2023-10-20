#!/usr/bin/python3
'''Starts a Flask web application:
    - must be listening on 0.0.0.0 and port 5000
    - route '/' must display "Hello HBNB!"
    - route '/hbnb' must display "HBNB!"
    - route '/c/<text>' displays "C" followed by the value of text
        (replace underscore '_' in text with '')
    - route '/python/<text>' displays "Python" followed by the value of text
        - the default value of text is "is cool"
        (replace underscore '_' in text with '')
    - route 'number/<n>': displays "n is a number" only if n is an integer
    - must use the option 'strict_slashes=False' in each route definition
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
    '''displays "C", followed by the value of text variable
        (replace '_' in text with ' ')
    '''
    new_text = text.replace('_', ' ')
    return f'C {new_text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    '''displays "Python", followed by the value of text variable
        - the default value of text is "is cool"
        (replace '_' in text with ' ')
    '''
    if len(text) > 0:
        new_text = text.replace('_', ' ')
    return f'Python {new_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' displays "n is a number" only if argument n is an integer
    '''
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
