#!/usr/bin/python3
"""
This module contains a Flask web application instance.

The instance listens on 0.0.0.0, port 5000.

Routes:
    /states: displays a list of all State objects present in DBStorage sorted by name (A->Z).
    /states/<id>: displays a page with the State object matching the provided id and its linked City objects.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
    Displays a HTML page:
    - If id is None: displays a list of all State objects present in DBStorage sorted by name (A->Z).
    - If id is provided: displays a page with the State object matching the id and its linked City objects.
        - If no State object is found with the provided id, displays "Not found!".
    """
    states = storage.all(State)
    if id:
        key = "{}.{}".format(State.__name__, id)
        if key in states:
            states = {key: states[key]}
        else:
            states = {}
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close_session(exception):
    """
    Removes the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

