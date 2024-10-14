#!/usr/bin/env python3
""" Auth class for API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv

User = TypeVar('User')


class Auth:
    """ Class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if a path requires authentication
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'

            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get the Authorization header from the request
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user from the request
        """
        return None

    def session_cookie(self, request=None):
        """ Return the value of the session cookie from the request """
        if request is None:
            return None

        # Get the session cookie name from the environment variable
        # SESSION_NAME
        session_name = getenv('SESSION_NAME')

        if session_name is None:
            return None

        # Retrieve the cookie value from the request using the session_name
        return request.cookies.get(session_name, None)
