#!/usr/bin/python3
'''Starts a web application listening on 0.0.0.0 and port 5000
    - To load all cities of a State:
        - If storage engine is DBStorage, you must use cities relationship
        - Otherwise, use the public getter method cities
    - Routes:
        - /cities_by_states: display a HTML page: (inside the tag BODY)
        - UL tag: with the list of all State objects present in DBStorage
            sorted by name
            - LI tag: description of one State: <state.id>: <B><state.name></B>
                + UL tag: with
                    - LI: description of a City: <city.id>: <B><city.name></B>
'''

from models import storage
from flask import Flask, render_template
import sys
sys.path.append('../')

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''
        - displays a HTML page: (inside the tag BODY)
        - UL tag: with the list of all State objects present in DBStorage
            sorted by name
            - LI tag: description of one State: <state.id>: <B><state.name></B>
                + UL tag: with
                    - LI: description of a City: <city.id>: <B><city.name></B>
    '''
    return render_template('8-cities_by_states.html',
                           states=storage.all("State").values())


@app.teardown_appcontext
def teardown(self):
    '''removes the current SQLAlchemy Session after each request
    '''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=1)
