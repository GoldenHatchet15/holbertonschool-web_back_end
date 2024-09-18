#!/usr/bin/env python3
""" FIFO Cache module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system """

    def __init__(self):
        """ Initialize the class by calling the parent init """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO """
        if key is None or item is None:
            return

        if (key not in self.cache_data and
                len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            first_key = self.order.pop(0)
            # Remove the oldest item (first added)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

        # Add the key to the order list,
        # maintain its position or update it if it exists
        if key not in self.order:
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
