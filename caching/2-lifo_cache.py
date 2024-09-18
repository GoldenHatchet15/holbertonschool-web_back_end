#!/usr/bin/env python3
""" LIFO Cache module """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize the class by calling the parent init """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache using LIFO """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
