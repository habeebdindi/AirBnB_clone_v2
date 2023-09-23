#!/usr/bin/python3
""" A script that starts a web flas application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function displays a text at the / of the website
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function displays a text at the /hbnb of the website
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """This function displays a text at the /c of the website
    """
    format_text = text.replace("_", " ")
    return "C {}".format(format_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
