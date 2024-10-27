#!/usr/bin/env python3
"""
Flask app with i18n support using Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)



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


def get_locale():
    """
    Determine the best match for supported languages based on request args
    and headers.

    Returns:
        str: The locale to be used for translations.
    """
    # Check if the 'locale' parameter is in the URL and is supported
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Fallback to the best match from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render the index page with translated text.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
