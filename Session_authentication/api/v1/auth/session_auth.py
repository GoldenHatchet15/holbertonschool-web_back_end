#!/usr/bin/env python3
""" Session authentication module """
from api.v1.auth.auth import Auth
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
