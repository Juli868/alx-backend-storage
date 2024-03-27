#!/usr/bin/env python3
"""Redis practices."""
import uuid as uuid
import redis
from typing import Union, Callable


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

    def get(self, key, fn: Callable = None) ->\
            Union[str, bytes, int, float, None]:
        """Find the wanted info using its key."""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return (data)

    def get_str(self, key: str) -> [str, None]:
        """Return a string according to the key given."""
        return self.get(
                        key, lambda x: x.decode("utf-8")
                        if isinstance(c, bytes) else x)

    def get_int(self) -> [int, None]:
        """Return the associated adata in int."""
        return self.get(key, lambda x: int(
            x.decode("utf-8") if isinstance(c, bytes) else x))
