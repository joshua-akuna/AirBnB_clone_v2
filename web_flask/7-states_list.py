#!/usr/bin/python3
'''Starts a Flask web application that listens on 0.0.0.0 and port 5000
    - You must use storage for fetching data from the storage engine
    - After each request, you must remove the current SQLAlchemy Session:
        - Declare a method to handle @app.teardown_appcontext
        - Call in this method storage.close()
    - Routes
        - /states_list: displays a HTML page
'''

from flask import Flask, render_template
from models import storage
import sys
sys.path.append("../")

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    ''' displays a HTML page
        - H1 tag: "States"
        - UL tag: with the list of all State objects present in DBStorage
            sorted by name
    '''
    return render_template("7-states_list.html", states=storage.all("State"))


@app.teardown_appcontext
def tear_down(self):
    '''calls the close method on the storage instance
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)
