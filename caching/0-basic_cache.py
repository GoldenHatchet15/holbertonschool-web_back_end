#!/usr/bin/env python3
""" BasicCache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system without limit """

    def put(self, key, item):
        """ Assign the item value for the key in self.cache_data """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to key in self.cache_data """
        return self.cache_data.get(key, None)
