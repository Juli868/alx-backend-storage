#!/usr/bin/env python3
"""Redis practices."""
import uuid as uuid
import redis
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """Count how many the methods are called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"calls:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache():
    """Cache using Redis."""

    def __init__(self):
        """Class definition."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
