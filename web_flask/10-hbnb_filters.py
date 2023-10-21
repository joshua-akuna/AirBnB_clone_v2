#!/usr/bin/python3
'''The script starts a web application listening on 0.0.0.0, port 5000
    - To load all cities of a state:
        - If storage engine is DBStorage, you must use cities relationship
        - Otherwise, use the public getter method cities
    - After each request you must remove the current SQLAlchemy Session:
        - Declare a method to handle @app.teardown_appcontext
        - Call in this method storage.close()
    - You must use the option strict_slashes=False in your route definition
'''

import sys
sys.path.append("../")

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb')
def hbnb():
    '''
    '''
    return render_template("10-hbnb_filters.html",
                            states=storage.all("State"),
                            amenities=storage.all('Amenity'))


@app.teardown_appcontext
def teardown(self):
    '''Removes the current SQLAlchemy Session after each request
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
