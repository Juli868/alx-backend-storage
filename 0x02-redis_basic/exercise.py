#!/usr/bin/env python3
"""Redis practices."""
import uuid as uuid
import redis
from typing import Union


class Cache():
    """Cache using Redis."""

    def __init__(self):
        """Class definition."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data given."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
