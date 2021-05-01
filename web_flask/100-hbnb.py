#!/usr/bin/python3
""" flask module """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

storage.all()
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return all states in the db  """
    states = storage.all(State).values()  # list
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    print(places)
    return render_template('100-hbnb.html',
                           states=states,
                           places=places,
                           amenities=amenities)


@app.teardown_appcontext
def close_session(ctx):
    """ this function get called when the context is popped
        the context get popped when the request is finished
    """
    storage.close()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=1)
