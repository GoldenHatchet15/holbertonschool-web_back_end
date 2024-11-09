#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis.
"""

import redis
import uuid
from typing import Union

class Cache:
    """Cache class to handle storing and retrieving data in Redis."""
    
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key.

        Args:
            data (Union[str, bytes, int, float]): Data to store in Redis.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())  # Generate a random UUID as the key
        self._redis.set(key, data)  # Store data in Redis with the generated key
        return key
