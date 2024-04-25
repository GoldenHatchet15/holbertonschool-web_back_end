#!/usr/bin/env python3
"""
This module contains a type-annotated function 'sum_list'
that sums a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of float numbers.

    Parameters:
    input_list (List[float]): A list of floats.

    Returns:
    float: The sum of the list elements.
    """
    return sum(input_list)
