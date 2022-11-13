#!/usr/bin/python3
"""Starts a web application using the Flask framework"""

from flask import Flask, render_template, Markup

from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    all_states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    all_states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    places.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    content = {
        'states': all_states,
        'amenities': amenities,
        'places': places
    }
    return render_template('100-hbnb.html', **content)


@app.teardown_appcontext
def app_teardown(self):
    """Removes the current SQL Alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
