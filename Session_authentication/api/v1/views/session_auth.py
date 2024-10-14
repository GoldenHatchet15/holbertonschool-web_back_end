#!/usr/bin/env python3
""" Session authentication view module """
from flask import jsonify, request, abort
from models.user import User
from api.v1.views import app_views
from os import getenv
from api.v1.app import auth  
# Import auth only where needed to avoid circular imports

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles user login via session authentication"""
    
    # Retrieve email and password from the request
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Validate that email and password are provided
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    
    # Retrieve the User instance based on the email
    try:
        users = User.search({"email": email})
    except Exception:
        users = None

    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    
    user = users[0]

    # Check if the password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    
    # Create a session ID for the User
    session_id = auth.create_session(user.id)
    
    # Prepare the response and set the session cookie
    response = jsonify(user.to_json())
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)
    
    return response
