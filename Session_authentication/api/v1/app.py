#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from api.v1.views import app_views
from api.v1.auth.auth import Auth  # Import the Auth class
from api.v1.auth.basic_auth import BasicAuth  # Import the BasicAuth class
from api.v1.auth.session_auth import SessionAuth  # Import the SessionAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
AUTH_TYPE = getenv("AUTH_TYPE", None)

if AUTH_TYPE == "basic_auth":
    auth = BasicAuth()
elif AUTH_TYPE == "session_auth":  # New switch for session_auth
    auth = SessionAuth()
elif AUTH_TYPE == "auth":
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """ Filter requests based on authentication """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/'  # Add the login path to excluded paths
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    # If both the authorization header and session cookie are None, abort with
    # 401
    if auth.authorization_header(
            request) is None and auth.session_cookie(request) is None:
        abort(401)

    request.current_user = auth.current_user(request)

    if request.current_user is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
