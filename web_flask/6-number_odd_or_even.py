#!/usr/bin/python3

"""
starts a flask web application
"""

from flask import Flask, render_template
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
def python(text='is cool'):
    """ display python with value of text variable"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def numb(n):
    """ display value of n var if it is int"""
    return '{:d} is number'.format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """ display template n var if it is int """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """ return template if n is int and check odd|even"""
    if (n % 2 == 0):
        var = 'even'
    else:
        var = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, var=var)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
