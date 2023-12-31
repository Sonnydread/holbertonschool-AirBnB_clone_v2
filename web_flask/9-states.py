#!/usr/bin/python3
"""Flask web appl"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """list of states"""
    return render_template("9-states.html",
                           data1=storage.all(State),
                           data3=None)


@app.route("/states/<id>", strict_slashes=False)
def statesoflist(id):
    """list of cities"""
    return render_template("9-states.html",
                           data1=storage.all(State),
                           data2=storage.all(City),
                           data3=id)


@app.teardown_appcontext
def close(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
