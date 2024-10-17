#!/usr/bin/env python3
"""
Flask app for user registration and login
"""
from flask import Flask, request, jsonify, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/users', methods=['POST'])
def register_user():
    """POST /users route to register a new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """POST /sessions route to log in a user and create a session"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(401)

    # Check if the login is valid
    if not AUTH.valid_login(email, password):
        abort(401)

    # Create a session and store the session ID as a cookie
    session_id = AUTH.create_session(email)
    if not session_id:
        abort(401)

    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
