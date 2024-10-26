#!/usr/bin/env python3
"""
Flask app with i18n support using Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """
    Configuration class for Babel and Flask app.

    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default language locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """
    Determine the best match for supported languages based on request headers.

    Returns:
        str: Best matching language from the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render the index page with translated text.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
