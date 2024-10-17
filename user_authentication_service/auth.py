#!/usr/bin/env python3
"""
Auth module for user authentication
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes a password with bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """Generate a new UUID and return it as a string"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with email and password"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(
                'utf-8'), user.hashed_password)
        except (NoResultFound, ValueError):
            return False

    def create_session(self, email: str) -> str:
        """Create a session ID for the user and return it

        Args:
            email (str): The user's email

        Returns:
            str: The session ID or None if the user doesn't exist
        """
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            # Generate a new session ID
            session_id = _generate_uuid()
            # Update the user's session_id in the database
            self._db.update_user(user.id, session_id=session_id)
            # Return the session ID
            return session_id
        except NoResultFound:
            return None
