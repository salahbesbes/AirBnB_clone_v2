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


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def optional_arg(text='cool'):
    """ pass argument to route """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
