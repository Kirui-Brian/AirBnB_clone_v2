#!/usr/bin/python3
"""
This module contains a Flask instance.

The instance listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns the string "Hello HBNB!" when accessing the root '/'.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns the string "HBNB" when accessing the '/hbnb' path.
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function returns the string "C" followed by the value of the text variable
    when accessing the '/c/<text>' path. Underscore symbols in the text variable
    are replaced with a space.
    """
    return "C " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
