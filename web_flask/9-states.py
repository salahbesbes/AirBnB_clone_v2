#!/usr/bin/python3
""" flask module """
from flask import Flask, render_template
import models
from models.state import State
from models import storage

storage.all()
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """ return single state description """
    found_state = None
    states = storage.all(State).values()  # list of states instance
    if id:
        for state in states:
            if state.id == id:
                found_state = state
                break
        return render_template('9-states.html',
                               states=states,
                               state=found_state,
                               show_cities=True)

    return render_template('9-states.html',
                           states=states,
                           state=found_state,
                           show_cities=False)


@app.teardown_appcontext
def close_session(ctx):
    """ this function get called when the context is popped
        the context get popped when the request is finished
    """
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
