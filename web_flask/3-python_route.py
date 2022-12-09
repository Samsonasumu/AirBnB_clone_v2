#!/usr/bin/python3

"""
starts a flask web application
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ returns a message"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """new path"""
    return ("HBNB")


@app.route('/c/<text>')
def c(text):
    """ display C with value in variable text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def pythoncool(text='is cool'):
    """display python with value of text variable"""
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
