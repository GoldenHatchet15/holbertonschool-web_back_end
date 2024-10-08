#!/usr/bin/env python3
"""
Encrypting and validating passwords module using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt's hashpw function with a salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password as a byte string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain-text password to validate.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    # Use bcrypt's checkpw to verify
    # if the password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
