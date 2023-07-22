#!/usr/bin/env python3
""" Define a class 'cache' """
import redis
from typing import Union
import uuid


class Cache:
    """ create a class cache """
    def __init__(self):
        """ initialize the cache instace """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ A menthod that generate a random key stores the input
            data in redisusing a random key and returns the key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
