#!/usr/bin/python3
"""
Start my web app
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=false)
def home():
    """
    home function
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
