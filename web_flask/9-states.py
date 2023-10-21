#!/usr/bin/python3
'''The script starts a Flask web application listening on 0.0.0.0, port 5000
    - To load all cities of a State
        - If your storage engine is DBStorage, you must use cities relationship
        - Otherwise, use the public getter method cities
    - After each request you must remove the current SQLAlchemy Session:
        - Declare a method to handle @app.teardown_appcontext
        - Call in this method storage.close()
    - You must use the option strcit_slashes=False in your route definition
'''

from models import storage
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    '''Routes
        /states: displays a HTML page: (inside the tag BODY)
            - H1 tag: "States"
            - UL tag: list all State objects present in
                DBStorage sorted by name
                -LI tag: describes one State: <state.id>: <B><statename></B>
        /states/<id>: display a HTML page: (inside the tag BODY)
            - If a State object is found with id:
                - H1 tag: "State"
                - H3 tag: "Cities"
                - UL tag: with the list of City objects linked to the
                    State sorted by name
                    -LI tag: description of one City: <city.id>: <B><city.name><B/>
    '''
    state = None
    if id is None:
        state = [value for value in storage.all("State").values()]
    else:
        states = [value for value in storage.all("State").values()
                if value.id == id]
        if len(states) > 0:
            state = states[0]
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(self):
    ''' Removes the current SQLAlchemy Session after each request
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
