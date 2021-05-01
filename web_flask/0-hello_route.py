#!/usr/bin/python3
""" flask module """
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ create home content """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
