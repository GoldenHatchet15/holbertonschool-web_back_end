#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            self.__indexed_dataset = {
                i: row for i, row in enumerate(self.dataset())
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Fetch a page with a specified size from an indexed dataset,
        accounting for deletions.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing the index,
            data, page size, next index.
        """
        if index is None:
            index = 0
        assert 0 <= index < len(self.__indexed_dataset), "Index out of range."

        dataset = self.indexed_dataset()
        keys = sorted(dataset.keys())  # Get sorted list of existing indexes
        data = []

        current_index = index
        while len(data) < page_size and current_index <= max(keys):
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        next_index = current_index if current_index < max(keys) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }


if __name__ == "__main__":
    server = Server()
    server.indexed_dataset()

    try:
        server.get_hyper_index(300000, 100)
    except AssertionError:
        print("AssertionError raised when out of range")

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index
    print(server.get_hyper_index(res.get('next_index'), page_size))
