#!/usr/bin/env python3
"""
Module to calculate index range for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a page of items.

    Args:
    page (int): The current page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index
    and the end index of the items for the requested page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


if __name__ == "__main__":
    # Testing the function with example inputs
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
