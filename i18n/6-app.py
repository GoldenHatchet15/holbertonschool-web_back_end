#!/usr/bin/env python3
"""
Flask app with i18n support using Flask-Babel and mock login.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel()


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


def get_user():
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


def get_locale():
    """
    Determine the best match for supported languages based on priority:
    URL parameter, user settings, request headers, default.

    Returns:
        str: The locale to be used for translations.
    """
    # 1. Check URL parameter
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # 2. Check user settings if logged in
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # 3. Fallback to request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """
    Render the index page with translated text.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
