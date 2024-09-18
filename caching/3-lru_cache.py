#!/usr/bin/env python3
""" LRU Cache module """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Initialize the class by calling the parent init """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU """
        if key is None or item is None:
            return

        # If the key exists, update its position
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the least recently used item (first in the list)
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new key and update its position in the order list
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key, and update
        its position as most recently used """
        if key is None or key not in self.cache_data:
            return None

        # Update key position in the order list
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
