#!/usr/bin/python3
""" 0. Script to start a Flask web application """

from flask import Flask, render_template


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
    return 'C {}'.format(text_trimmed)


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Returns some text. """
    text_trimmed = text.replace('_', ' ')
    return 'Python {}'.format(text_trimmed)


@app.route('/number/<int:n>', strict_slashes=False)
def numberFunction(n):
    """ Returns some the number only if int. """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render a template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
