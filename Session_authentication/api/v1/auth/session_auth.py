#!/usr/bin/env python3
""" Session authentication module """
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Session authentication class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a session ID for a given user ID """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the session ID with the corresponding user ID
        self.user_id_by_session_id[session_id] = user_id

        # Return the session ID
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieve the user ID based on the session ID """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Retrieve the User instance
        based on the session ID from the cookie """
        if request is None:
            return None

        # Get the session ID from the cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Get the user ID using the session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        # Retrieve the User instance from the database using the user ID
        return User.get(user_id)
