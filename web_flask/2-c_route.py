#!/usr/bin/python3
""" 0. Script to start a Flask web application """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return “HBNB”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cistext(text):
    """ Returns some text. """
    text_trimmed = text.replace('_', ' ')
    return 'c {}'.format(text_trimmed)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
