#!/usr/bin/python3
"""Starts a web application using the Flask framework"""

from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """The state list page"""
    all_state_list = list(storage.all(State).values())
    return render_template('7-states_list.html', all_state_list)


@app.teardown_appcontext
def app_teardown(self):
    """Removes the current SQL Alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
