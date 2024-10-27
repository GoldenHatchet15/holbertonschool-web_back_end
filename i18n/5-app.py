#!/usr/bin/env python3
"""
Flask app with i18n support using Flask-Babel and mock login.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Union, Dict

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

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Retrieves a user based on the login_as URL parameter.

    Returns:
        dict or None: The user dictionary if found, None otherwise.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Executed before each request. Sets the user in flask.g if logged in.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages based on request args
    and headers.

    Returns:
        str: The locale to be used for translations.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page with translated text.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
