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
        """Create a session ID for the user and return it"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Find user by session ID"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session of a user by setting session_id to None"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for the user

        Args:
            email (str): The user's email

        Returns:
            str: The reset token

        Raises:
            ValueError: If the user does not exist
        """
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            # Generate a new UUID as the reset token
            reset_token = _generate_uuid()
            # Update the user's reset_token in the database
            self._db.update_user(user.id, reset_token=reset_token)
            # Return the reset token
            return reset_token
        except NoResultFound:
            raise ValueError(f"User with email {email} does not exist")
