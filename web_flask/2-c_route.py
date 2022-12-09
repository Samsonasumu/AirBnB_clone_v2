#!/usr/bin/python3

"""
starts a flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns a message"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """new path"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ display C with value in variable text"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
