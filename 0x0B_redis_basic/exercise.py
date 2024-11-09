#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and apply an optional conversion function.

        Args:
            key (str): The key of the data to retrieve.
            fn (Optional[Callable]): A function to convert the data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, potentially converted by fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            Optional[str]: The data decoded as a UTF-8 string, or None if not found.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            Optional[int]: The data converted to an integer, or None if not found.
        """
        return self.get(key, lambda d: int(d))
