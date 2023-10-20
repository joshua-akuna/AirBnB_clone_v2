#!/usr/bin/python3
'''The module defines a script that runs a Flask web application
    - app must be listening on 0.0.0.0 and port 500
    - route '/' must display 'hello HBNB!'
    - you must use the option 'strict_slashes=False' in route definition
'''
from flask import Flask

app = Flask(__name__)


app.route('/', strict_slashes=False)
def hello(self):
    '''returns 'hello HBNB! for the route '/''
    '''
    return "hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=1)
