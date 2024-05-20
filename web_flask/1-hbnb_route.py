#!/usr/bin/python3
"""
Flask Web Application Module

This module contains a Flask application instance that listens on all network
interfaces at port 5000. It defines two routes:

    1. '/' - returns "Hello HBNB!"
    2. '/hbnb' - returns "HBNB"
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Root route ('/') handler.

    This function is executed when a user accesses the root URL ('/').
    It returns the string "Hello HBNB!" as a response.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    '/hbnb' route handler.

    This function is executed when a user accesses the URL '/hbnb'.
    It returns the string "HBNB" as a response.
    """
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
