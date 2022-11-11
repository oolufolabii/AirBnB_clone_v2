#!/usr/bin/python3
"""Starts a web application using the Flask framework"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index_page():
    """The index/home page
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """The HBNB page
    """
    return "HBNB"


@app.route('/c/<text>')
def c_page(text):
    """The C page
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    """The python page
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def num(n):
    """The number page
    """
    if type(n) == int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    '''The number_template page.'''
    ctxt = {
        'n': n
    }
    return render_template('5-number.html', **ctxt)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    """The odd or even number template"""
    if type(n) == int:
        ctxt = {
            'n': n
        }
        return render_template('6-number_odd_or_even.html', **ctxt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
