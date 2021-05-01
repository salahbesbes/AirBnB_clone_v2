#!/usr/bin/python3
""" flask module """
from flask import Flask, escape, request

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


@app.route('/number/<int:n>', strict_slashes=False)
def return_number(n):
    """ pass int argument to route """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
