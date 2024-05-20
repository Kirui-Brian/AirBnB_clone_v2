#!/usr/bin/python3
"""
This module contains a Flasj instance.

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

@pp.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function returns the string "C" followed by the value of the text variable when accessing the '/c/<text>' path.
    Underscore symbols in the text variable are replaced with a space.
    """
    return "C" + text.replace("_", " ")

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyhton_text(text):
    """
    This function returns the string "Python " followedby the value of the text variable when accessing the '/python/<text>' path.
    Underscore symbols in the text variable are replaced with a space.
    The default value of text is "is cool".
    """
    return "Python " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
