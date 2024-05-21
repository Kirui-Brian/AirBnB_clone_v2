#!/usr/bin/python3
"""
Module: flask_app

This module starts a Flask web application on localhost. It uses a storage
engine to retrieve data and renders templates to display the data.

Routes:
    /states_list: Displays a list of states using a template.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """
    Called on teardown of app contexts. For more info on contexts visit:
    http://flask.pocoo.org/docs/1.0/appcontext/

    Storage.close() closes the SQL scoped session or reloads file storage.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def conditional_templating(n=None):
    """
    Displays a list of states using a template.

    Parameters:
        n: An optional parameter (default is None).

    Returns:
        A rendered HTML template.
    """
    return render_template('7-states_list.html', states=storage.all("State"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
