#!/usr/bin/python3
"""Simple Flask app, with additional route"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def run_all_states():
    """Run all states"""
    l_list = storage.all(State)
    return render_template('7-states_list.html', l_list=l_list)


@app.teardown_appcontext
def do_teardown(self):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
