#!/usr/bin/env python3
""" MRU Cache module """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching system """

    def __init__(self):
        """ Initialize the class by calling the parent init """
        super().__init__()
        self.order = []  # List to track the access order of keys

    def put(self, key, item):
        """ Add an item in the cache using MRU """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item (last in the list)
            mru_key = self.order.pop()
            # The last item is the most recently used
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the new key and update its position in the order list
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key,
        and mark it as the most recently used """
        if key is None or key not in self.cache_data:
            return None

        # Update key position in the order list as the most recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
