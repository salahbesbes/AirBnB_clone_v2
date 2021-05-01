#!/usr/bin/python3
""" flask module """
from flask import Flask, render_template
import models
from models.state import State

storage = models.storage
storage.all()
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ return all states in the db  """
    states = storage.all(State)  # dict
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_list(id):
    """ return single state description """
    found_state = None

    states = storage.all(State).values()  # list of states instance
    for state in states:
        if state.id == id:
            found_state = state
            break
    return render_template('9-states.html', state=found_state)


@app.teardown_appcontext
def close_session(ctx):
    """ this function get called when the context is popped
        the context get popped when the request is finished
    """
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
