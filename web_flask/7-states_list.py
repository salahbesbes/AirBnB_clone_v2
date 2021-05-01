#!/usr/bin/python3
""" flask module """
from flask import Flask, render_template
import models
from models.state import State

storage = models.storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ return all states in the db  """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(ctx):
    """ this function get called when the context is popped
        the context get popped when the request is finished
    """
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
