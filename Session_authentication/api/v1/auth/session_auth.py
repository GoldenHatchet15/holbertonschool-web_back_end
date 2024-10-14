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

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieve the user ID based on the session ID """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def destroy_session(self, request=None) -> bool:
        """ Deletes the user session / logs out the user """
        if request is None:
            return False

        # Get the session ID from the cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Check if session ID exists in the dictionary
        if self.user_id_for_session_id(session_id) is None:
            return False

        # Delete the session ID
        del self.user_id_by_session_id[session_id]
        return True
