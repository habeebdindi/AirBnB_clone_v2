#!/usr/bin/python3
""" starts a flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """ Fetch cities and states from storage, place in rendered template """
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """ close SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
