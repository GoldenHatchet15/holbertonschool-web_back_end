#!/usr/bin/env python3
"""
Encrypting passwords module using bcrypt
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
