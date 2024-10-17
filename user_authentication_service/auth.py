#!/usr/bin/env python3
"""
Auth module for user authentication
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes a password with bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


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
        """Validate login credentials

        Args:
            email (str): User's email
            password (str): User's password

        Returns:
            bool: True if login is valid, False otherwise
        """
        try:
            # Find user by email
            user = self._db.find_user_by(email=email)
            # Check if password matches
            return bcrypt.checkpw(password.encode(
                'utf-8'), user.hashed_password)
        except (NoResultFound, ValueError):
            # Return False if user not found or any error occurs
            return False
