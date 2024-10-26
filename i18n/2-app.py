#!/usr/bin/env python3
"""Start a basic Flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Babel and Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.locale_selector
def get_locale():
    """
    Determine the best match
    for supported languages based
    on request headers.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route to render the index page."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
