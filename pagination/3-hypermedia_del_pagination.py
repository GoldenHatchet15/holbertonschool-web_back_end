#!/usr/bin/env python3
"""
Module for hypermedia pagination of a dataset of popular baby names.
"""

import csv
import math
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names with hypermedia."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.

        Returns:
            List[List]: The dataset loaded from the CSV file, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, mode='r', newline='') as f:
                reader = csv.reader(f)
                self.__dataset = list(reader)[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Fetch a page of the dataset with a specified number of entries.

        Args:
            page (int): The page number, starting from 1.
            page_size (int): The number of items on each page.

        Returns:
            List[List]: A list of rows from the dataset representing the page.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index] if start_index < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Get a page of the dataset along with hypermedia information.

        Args:
            page (int): Current page number.
            page_size (int): Number of items per page.

        Returns:
            Dict: A dictionary with pagination and hypermedia information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
