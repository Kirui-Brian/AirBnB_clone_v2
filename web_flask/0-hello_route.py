#!/usr/bin/python3
"""
This module contains a Flask instance.
The instance  listens on 0.0.0.0, port 5000.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This finction returns the string "Hello HBNB! when accessing the root '/'.
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
