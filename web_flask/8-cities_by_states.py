#!/usr/bin/python3
"""Starts a web application using the Flask framework"""

from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """Cites sorted by states page"""
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda a: a.name)
    for state in all_states:
        state.cities.sort(key=lambda y: y.name)

    content = {
        'states': all_states
    }

    return render_template('8-cities_by_states.html', **content)


@app.teardown_appcontext
def app_teardown(self):
    """Removes the current SQL Alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
