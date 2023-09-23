#!/usr/bin/python3
""" A script that starts a web flas application
"""
from flask import Flask, url_for, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    """This function displays a text at the /python of the website
    """
    format_text = text.replace("_", " ")
    return "Python {}".format(format_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """This function displays a text at the /number/n of the website
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """This function displays a text at the /number/n of the website
       using a template.
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
