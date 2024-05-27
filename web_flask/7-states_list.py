#!/usr/bin/python3
"""
This module starts a Flask web application.

The application serves a webpage that lists states in alphabetical order.

Functions:
    states_list(): Renders a HTML page with states listed in alphabetical order.
    teardown_db(exception): Closes the storage on teardown.

Routes:
    /states_list: URL for the states_list() function.

App Context:
    teardown_db(exception): Called after the response has been constructed and sent to the client.
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a HTML page with the states listed in alphabetical order.

    Retrieves all State objects from storage,
    sorts them in alphabetical order,
    and passes them to the '7-states_list.html' template to be rendered.

    Returns:
        Rendered template '7-states_list.html'.
    """
    states = sorted(
            list(storage.all("State").values()), key=lambda x: x.name
            )
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.

    This function is called after the response has been
    constructed and sent to the client.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
