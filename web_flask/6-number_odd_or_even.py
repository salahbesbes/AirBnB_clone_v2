#!/usr/bin/python3
""" flask module """
from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ create home content """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ test routes """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def pass_arg(text):
    """ pass argument to route """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/(<text>)', strict_slashes=False)
def pass_new_arg(text='cool'):
    """ pass argument to route """
    return 'python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def return_number(n):
    """ pass int argument to route """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_page_number(n):
    """ pass int argument to route """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ pass int argument to route """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
