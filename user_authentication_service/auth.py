#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password with bcrypt

    Args:
        password (str): The password to be hashed

    Returns:
        bytes: The hashed password as bytes
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
