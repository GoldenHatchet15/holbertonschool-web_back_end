#!/usr/bin/env python3
""" BasicAuth class for basic authentication
"""
from typing import TypeVar, Optional, Tuple
import base64
from models.user import User
from api.v1.auth.auth import Auth

# Declare the User TypeVar
U = TypeVar('User', bound=User)


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """ Extracts the Base64 part of the Authorization header """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """ Decodes the Base64 part of the Authorization header """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Extracts the user email and password from the decoded Base64 value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> U:
        """ Returns the User instance based on the email and password """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Search for the user by email
        users = User.search({"email": user_email})
        if not users:
            return None

        user = users[0]

        # Check if the password is valid
        if user.is_valid_password(user_pwd):
            return user

        return None


    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """Extracts the user email and password from the decoded Base64 value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def current_user(self, request=None) -> U:
        """ Retrieves the User instance for a request """
        # Get Authorization header
        auth_header = self.authorization_header(request)
        print(f"Authorization header: {auth_header}")
        if auth_header is None:
            return None

        # Extract Base64 part of the header
        base64_auth = self.extract_base64_authorization_header(auth_header)
        print(f"Base64 Authorization header: {base64_auth}")
        if base64_auth is None:
            return None

        # Decode Base64
        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        print(f"Decoded Authorization header: {decoded_auth}")
        if decoded_auth is None:
            return None

        # Extract user credentials (email and password)
        email, password = self.extract_user_credentials(decoded_auth)
        print(f"User email: {email}, Password: {password}")
        if email is None or password is None:
            return None

        # Retrieve the user object from credentials
        user = self.user_object_from_credentials(email, password)
        print(f"Authenticated User: {user}")
        return user
