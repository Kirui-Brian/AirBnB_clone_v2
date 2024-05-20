#!/usr/bin/python3
"""
Flask Web Application Module

This module contains a Flask application instance that listens on all
network interfaces at port 5000. It defines two routes:

    1. '/' - returns "Hello HBNB!"
    2. '/hbnb' - returns "HBNB"
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns the string "Hello HBNB!" when accessing the root '/'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns the string "HBNB" when accessing the '/hbnb' path
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
